def numberRange():
	x = int(raw_input('Enter a number: '))
	rnd = 0
	print rnd	#Prints first number.
	for rnd in range(x):
		print (rnd+1)	#Prints till the end of number.		

numberRange()