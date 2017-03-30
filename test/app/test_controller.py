import unittest


class TestController(unittest.TestCase):


  @classmethod
  def setUp(cls):
    # region register app home path ref. http://flask.pocoo.org/docs/0.11/deploying/mod_wsgi/#creating-a-wsgi-file
    import os
    import sys
    cd = os.path.abspath(os.path.dirname(__file__))
    APP_HOME = os.path.abspath('%s/../..' % cd)
    sys.path.insert(0, APP_HOME)
    # endregion register app home path

    #load test client
    from app import app
    cls.testClient = app.test_client()


  def test_app_try_model_noMocking(self):
    #region get output
    r = self.testClient.get('/app_try_model')

    #convert json to dict
    from flask import json
    d = json.loads(r.data)
    #endregion get output

    #assert actual vs expected
    self.assertIsNotNone(d)
    self.assertTrue(len(d)==2)
    for i in d:
      self.assertIsNotNone(i['name'])

