import unittest
from unittest.mock import MagicMock
from task_2 import Model


class TestMo(unittest.TestCase):

	def setUp(self):
		self.view = MagicMock()
		self.view.E.get = MagicMock(return_value="QWERTY")
		self.view.L = {}
		self.model = Model()
		self.model.setup(self.view)

	def test_A(self):
		assert self.model.view is self.view

	def test_B(self):
		self.model.copy()
		self.view.E.get.assert_called_once()
		self.assertEqual(self.view.L['text'], "QWERTY")