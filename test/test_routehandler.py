import unittest
from py_router import RouteHandler

class TestRouter(unittest.TestCase):
    def setUp(self):
      self.handler = RouteHandler()

    def test_class_init(self):
      paths = self.handler.Router.paths
      middlewares = self.handler.Router.middlewares
      self.assertEqual(paths, {})
      self.assertEqual(middlewares, [])

    def test_executeMiddlewares(self):
      self.handler.Router.use(lambda data, *others: data)
      data = self.handler.executeMiddlewares({ 'path': '/' })
      self.assertEqual(data, [{ 'path': '/' }])

    def test_executeMiddlewares_should_modifydata(self):
      def method(data, *others):
        data['method'] = 'get'
        return data
      self.handler.Router.use(method)
      data = self.handler.executeMiddlewares({ 'path': '/' })
      self.assertIn({ 'path': '/', 'method': 'get' }, data )

    def test_executerouteHandler(self):
      def method(req, *other):
        req['message'] = 'Hello World'
        return req['message']
      self.handler.Router.get('/', method)
      data = self.handler.executeRouteHandlers({ 'path': '/' })
      self.assertEqual(data, ['Hello World'])

    def test_handleRequest(self):
      def method(req, *other):
        req['message'] = 'Hello World'
        return req['message']
      self.handler.Router.get('/', method)
      data = self.handler.handleRequest({ 'path': '/' }, method)
      self.assertEqual(data, ['Hello World'])

    def test_register(self):
      def method(req, *other):
        req['message'] = 'Hello World!!'
        return req['message']
      self.handler.Router.get('/', method)
      data = self.handler.register()({ 'path': '/' }, method)
      self.assertEqual(data, ['Hello World!!'])

    def test_register_AwsLambdaMode(self):
      def method(req, *other):
        req['message'] = 'Hello World from post!!'
        return req['message']
      self.handler.Router.post('/', method)
      data = self.handler.register('aws-lambda')({ 'path': '/', 'httpMethod': 'POST' }, method)
      self.assertEqual(data, ['Hello World from post!!'])
    
