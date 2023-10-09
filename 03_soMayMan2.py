if __name__ == '__main__':
	# nhập số lần muốn nhập các số
	n=int(input('Enter n: '))
	# hàm giải
	def solve():
		# nhập vào các số
		s=str(input('Enter number: '))
		# tính độ dài của số đó
		length=int(len(s))
		# khởi tạo 1 cái tổng=0
		sum=0
		# chạy để lấy từng số theo giá trị index
		for j in range (0,length):
			# tổng các chữ số của số đã nhập vd 666 => 6+6+6 = 18 
			sum+=int(s[j])
			
			if sum==9:
				return 1
			else:

	# chạy số lần đã nhập
	for i in range (1,n+1):
		solve()