#region register app home path ref. http://flask.pocoo.org/docs/0.11/deploying/mod_wsgi/#creating-a-wsgi-file
import os
import sys
APP_HOME = os.path.abspath( os.path.dirname(__file__) )
sys.path.insert(0, APP_HOME)
#endregion register app home path

from app import app as application

if __name__ == '__main__':
  application.run(host='0.0.0.0', debug=True, port=5000, threaded=True)