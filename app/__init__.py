from flask import Flask
app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/mock-FlaskSqlAlchemy?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


from controller import *