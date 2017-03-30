from flask import Flask
app = Flask(__name__)


from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/mock-FlaskSqlAlchemy?charset=utf8'
db.init_app(app)


@app.route('/')
def app_index():
  return 'Flask app index - hello!'


@app.route('/app_try_model')
def app_try_model():
  from app.model.some_model import SomeModel
  someModelALL = SomeModel.query.all()
  d = [someModel.name for someModel in someModelALL]
  return str(d)