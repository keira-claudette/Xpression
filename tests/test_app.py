from app import *
import unittest


class TestUser(unittest.TestCase):

    def test_attrbuite(self):
       self.assertTrue(hasattr(User,"id"))
       self.assertTrue(hasattr(User, "username"))
       self.assertTrue(hasattr(User, "email"))
       self.assertTrue(hasattr(User, "password"))










