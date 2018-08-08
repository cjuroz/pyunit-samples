import unittest
from numberstest import NumbersTest

suite = unittest.TestSuite()
suite.addTest(NumbersTest("test_divide_byzero"))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
