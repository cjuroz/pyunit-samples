import unittest
from numberstest import NumbersTest
	
class UnitTests():
	
	def main():
		loader = unittest.TestLoader()
		suite = unittest.TestSuite()
		suite.addTests(loader.loadTestsFromModule(NumbersTest))

		runner = unittest.TextTestRunner(verbosity=3)
		result = runner.run(suite)
		
if __name__ == "__main__":
	unittest.main()