import unittest
from numberstest import NumbersTest

suite = unittest.TestSuite()
suite.addTest(NumbersTest("test_add"))
suite.addTest(NumbersTest("test_divide"))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
