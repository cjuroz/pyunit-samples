class Numbers():

	def add(self, num1, num2):
		sum = num1 + num2
		print("The sum of %s and %s is %s" %(num1, num2, sum))
		return sum		
		
	def divide(self, num1, num2):
		if num2 == 0:
			print("Division by zero is not supported yet...")
			return
		
		res = num1 / num2
		print("The division of %s and %s is %s" %(num1, num2, res))
		return res
