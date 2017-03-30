from app import app


@app.route('/')
def app_index():
  return 'Flask app index - hello!'


@app.route('/app_try_model')
def app_try_model():
  from app.model.some_model import SomeModel
  someModelALL = SomeModel.query.all()
  d = [someModel.name for someModel in someModelALL]
  return str(d)