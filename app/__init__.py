from flask import Flask
app = Flask(__name__)


from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/mock-FlaskSqlAlchemy?charset=utf8'
db.init_app(app)


from controller import *