from flask import Flask
app = Flask(__name__)


@app.route('/')
def app_index():
  return 'Flask app index - hello!'