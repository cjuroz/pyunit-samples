import unittest
from numberstest import NumbersTest
	
### NOT WORKING AS EXPECTED :( ###	
	
loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(NumbersTest)

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)