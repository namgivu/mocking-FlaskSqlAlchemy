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


  def test_app_try_model_withMocking(self):
    #set up expected
    from app.model.some_model import SomeModel
    o1 = SomeModel() ; o1.name = 'abb'
    o2 = SomeModel() ; o2.name = 'cdd'
    EXPECTED = dict()
    EXPECTED['d'] = [o1, o2]

    #set up mocking
    from mock import patch
    with patch('app.model.some_model.SomeModel') as model_mock:
      model_mock.query.all  \
        .return_value = EXPECTED['d']

      #region get output
      r = self.testClient.get('/app_try_model')

      #convert json to dict
      from flask import json
      d = json.loads(r.data)
      #endregion get output

    #assert actual vs expected
    self.assertIsNotNone(d)
    self.assertTrue(len(d)==2)
    e1 = d[0]
    e2 = d[1]
    self.assertEqual(e1['name'], o1.name)
    self.assertEqual(e2['name'], o2.name)

