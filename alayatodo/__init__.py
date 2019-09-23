from flask import Flask
from configs import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#login = LoginManager(app)
csrf = CSRFProtect(app)
jwt = JWTManager(app)

from alayatodo import views, models