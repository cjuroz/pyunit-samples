import unittest
from numberstest import NumbersTest
	
loader = unittest.TestLoader()
suite = unittest.TestSuite()	
suite.addTests(loader.loadTestsFromModule(NumbersTest))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)