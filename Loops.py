def main():
	x = 0
	
	#while example
	while(x<5):
		print(x)
		x = x+1
		
	#for example
	for x in range(5,10):
		print(x)
	
	#break and continue examples
	for x in range(5,10):
		#if(x==7): break
		if(x%2 == 0): continue
		print(x)
		
	#using enumerate
	days = ["Mon","Tue","Wed"]
	#enumerate fetches the index value
	for i,d in enumerate(days):
		print(i, d)

main()