def main():
	for i in incl_range(25):
		print(i, end = ' ')
	print()

#This function mocks the range function 
def incl_range(*args):
	numargs = len(args)
	start = 0
	step = 1
	#Parameters being initialized
	if numargs < 1:
		raise TypeError(f'Expected atleast 1 argument, got {numargs}')
	elif numargs == 1:
		stop = args[0]
	elif numargs == 2:
		(start, stop) = args
	elif numargs == 3:
		(start, stop, step) = args
	else: raise TypeError(f'Expected atmost 3 arguments, got {numargs}')
	#The real generator
	i = start
	while i <= stop:
		yield i
		i += step


main()
	