from app import app


@app.route('/')
def app_index():
  return 'Flask app index - hello!'


@app.route('/app_try_model')
def app_try_model():
  #query all model objects
  from app.model.some_model import SomeModel
  someModelALL = SomeModel.query.all()

  #output as json
  d = [dict(name=someModel.name) for someModel in someModelALL]
  from flask import jsonify
  return jsonify(d)  #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616