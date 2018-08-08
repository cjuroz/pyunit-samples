import unittest
from numbers import Numbers

class NumbersTest(unittest.TestCase):

	def test_add(self):
	
		num1 = 5
		num2 = 10
		total = 15
		
		res = Numbers().add(num1, num2)
		self.assertEqual(total, res)
		
	def test_divide(self):
		num1 = 10
		num2 = 5
		total = 2
		
		res = Numbers().divide(num1, num2)
		self.assertEqual(total, res) 
		
	def test_divide_byzero(self):
		num1 = 10
		num2 = 0
		total = 2
		
		res = Numbers().divide(num1, num2)
		self.assertTrue(res is None)
