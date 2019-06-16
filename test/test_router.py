import unittest
from py_router import Router

class TestRouter(unittest.TestCase):
    def setUp(self):
      self.router = Router()

    def test_class_init(self):
      paths = self.router.paths
      middlewares = self.router.middlewares
      self.assertEqual(paths, {})
      self.assertEqual(middlewares, [])

    def test_add_route(self):
      self.router.addRoute('/', 'get', lambda x: x)
      paths = self.router.paths
      self.assertIn('/', paths)

    def test_get_route(self):
      self.router.get('/', lambda x: x)
      paths = self.router.paths
      self.assertIn('/', paths)
      self.assertIn('get', paths['/'])

    def test_post_route(self):
      self.router.post('/', lambda x: x)
      paths = self.router.paths
      self.assertIn('/', paths)
      self.assertIn('post', paths['/'])

    def test_patch_route(self):
      self.router.patch('/', lambda x: x)
      paths = self.router.paths
      self.assertIn('/', paths)
      self.assertIn('patch', paths['/'])

    def test_put_route(self):
      self.router.put('/', lambda x: x)
      paths = self.router.paths
      self.assertIn('/', paths)
      self.assertIn('put', paths['/'])

    def test_all_route(self):
      self.router.all('/', lambda x: x)
      paths = self.router.paths
      self.assertIn('/', paths)
      self.assertIn('all', paths['/'])

    def test_use_route_no_path(self):
      self.router.use(lambda x: x)
      middlewares = self.router.middlewares
      self.assertEqual(len(middlewares), 1)

    def test_use_route_with_path(self):
      self.router.use('/', lambda x: x)
      middlewares = self.router.pathMiddlewares
      self.assertIn('/', middlewares)
      self.assertIsNotNone(middlewares['/'])


    
