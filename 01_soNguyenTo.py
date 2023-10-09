if __name__ == '__main__':
	import math
	a=int(input('Enter a: '))
	b=int(input('Enter b: '))
	def check(n):
		for j in range(2,n-1):
			if n%j==0:
				return False
		else:
			return True
	
	for i in range(a,b):
		if(check(i)==True):
			print(i)