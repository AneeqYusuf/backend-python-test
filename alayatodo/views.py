from alayatodo import app, models
from flask import (
    redirect,
    render_template,
    request,
    session,
    jsonify,
    url_for
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

@app.route('/todo/<id>/json', methods=['GET'])
def todo_json(id):
    todo = models.Todos.query.get(id).__repr__()
    return jsonify(todo)

@app.route('/todo', methods=['GET'])
@app.route('/todo/', methods=['GET'])
def todos():
    page = request.args.get('page', 1, type=int)    
    if not session.get('logged_in'):
        return redirect('/login')
    todos = models.Todos.query.paginate(page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('todos', page=todos.next_num) if todos.has_next else None
    prev_url = url_for('todos', page=todos.prev_num) if todos.has_prev else None
    return render_template('todos.html', todos=todos.items, empty=False, next_url = next_url, prev_url = prev_url)


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
    todos.status = 'incomplete'
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

@app.route('/todostatus/<id>', methods=['GET'])
def todo_update(id):
    if not session.get('logged_in'):
        return redirect('/login')
    todo = models.Todos.query.get(id)
    if (todo.status == 'complete'):
        todo.status = 'incomplete'
    else:
        todo.status = 'complete'
    models.db.session.commit()
    return redirect('/todo')
