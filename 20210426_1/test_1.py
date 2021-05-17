import unittest

from task_1 import solveSquare, wrongSolveSquare


class TestSquare(unittest.TestCase):

	# x^2 - 5*x + 6 = 0
	def test_D_positive(self):
		self.assertEqual(solveSquare(1, -5, 6), [2, 3])

	# x^2 + 2*x + 1 = 0
	def test_D_zero(self):
		self.assertEqual(solveSquare(1, 2, 1), [-1, -1])

	# 10*x^2 + x + 1 = 0
	def test_D_negative(self):
		self.assertEqual(solveSquare(10, 1, 1), None)

	def test_Foreign_1(self):
		self.assertFalse(wrongSolveSquare(2, 3, 1.125), [-0.75, -0.75])

	def test_Foreign_2(self):
		self.assertFalse(wrongSolveSquare(2, 3, 1), [-1, -0.5])

	def test_Foreign_3(self):
		self.assertFalse(wrongSolveSquare(2, 3, 4), None)