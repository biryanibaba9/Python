class myClass():
	def method1(self):
		print("Myclass method1")
		
	def method2(self, someString):
		print("Myclass method2 " + someString)

#Class inheriting from another class
class anotherClass(myClass):
	def method1(self):
		myClass.method1(self)
		print("an Myclass method1")
		
	def method2(self, someString):
		print("an Myclass method2 ")
		
def main():
	c = myClass()
	c.method1()
	c.method2("This is a string")
	
	c1 = anotherClass()
	c1.method1()
	c1.method2("This is a string")
		
main()