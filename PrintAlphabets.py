def letterRange():
	x = str(raw_input('Enter a start letter: '))
	d = ord(x)	#Converts the start letter input into its corresponding ASCII value
	y = str(raw_input('Enter an end letter: '))
	e = ord(y)	#Converts the end letter input to its corresponding ASCII value
	rnd = None
	print (x)	#Prints the first letter
	for rnd in range(d,e):
		print (chr(rnd+1))	#Converts the ascii back to char and prints it.			

letterRange()