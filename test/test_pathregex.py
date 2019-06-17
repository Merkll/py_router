import unittest
from py_router import PathMatch

class TestRouter(unittest.TestCase):
    def test_match(self):
      match = PathMatch().match('/users/:user/:about/:me', '/users/45/about/me/')
      self.assertIn('params', match)

    def test_match_wrong(self):
      match = PathMatch().match('/users/:user', '/users/45/about')
      self.assertIsNone(match)

    def test_multi_match(self):
      match = PathMatch().matchMulti(['/users/:user/:about/', '/users/:user/'], '/users/45/about/')
      self.assertEqual(match.get('path'), '/users/:user/:about/')

    def test_multi_match_no_match(self):
      match = PathMatch().matchMulti(['/users/:user/:about/', '/users/:user/'], '/users/')
      self.assertIsNone(match)
