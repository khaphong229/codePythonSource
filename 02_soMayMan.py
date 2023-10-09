if __name__ == '__main__':
	n=int(input('Enter n: '))
	
	def solve():
		s=str(input('Enter number: '))
		length=int(len(s))
		if(s[length-1]=='6' and s[length-2]=='8'):
			return 1
		else:
			return 0
		
	
	for i in range (1,n+1):
		print(solve())