from alayatodo import app, models
from flask import (
    redirect,
    render_template,
    request,
    session
    )


@app.route('/')
def home():
    with app.open_resource('../README.md', mode='r') as f:
        readme = "".join(l for l in f)
        return render_template('index.html', readme=readme)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_POST():
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = models.Users.query.filter_by(username=username).first()
    user.set_pass(password)
    models.db.session.commit()
    if(user.check_pass(password) == True):
        session['username'] = username
        session['logged_in'] = True
        return (redirect('/todo'))
    return (redirect('/login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect('/')

@app.route('/todo/<id>', methods=['GET'])
def todo(id):
    todo = models.Todos.query.get(id)
    return render_template('todo.html', todo=todo)


@app.route('/todo', methods=['GET'])
@app.route('/todo/', methods=['GET'])
def todos():
    if not session.get('logged_in'):
        return redirect('/login')
    todos = models.Todos.query.all()
    return render_template('todos.html', todos=todos, empty=False)


@app.route('/todo', methods=['POST'])
@app.route('/todo/', methods=['POST'])
def todos_POST():
    if not session.get('logged_in'):
        return redirect('/login')
    desc = request.form.get('description')
    if (desc == ''):
        todos = models.Todos.query.all()
        return render_template('todos.html', todos=todos, empty=True)
    todos = models.Todos()
    todos.user_id = models.Users.query.filter_by(username = session.get('username')).first().id
    todos.description = request.form.get('description', '')
    models.db.session.add(todos)
    models.db.session.commit()
    return redirect('/todo')


@app.route('/todo/<id>', methods=['POST'])
def todo_delete(id):
    if not session.get('logged_in'):
        return redirect('/login')
    models.db.session.delete(models.Todos.query.get(id))
    models.db.session.commit()
    return redirect('/todo')
