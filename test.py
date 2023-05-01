print('hello world')
print('this is a fibonnaci sequence implementation')

# TODO optimize this fibonnacci sequence function from O(N) to O(log N)
a,b = 0,1
for i in range(10):
	a,b = b,a+b
	print(b)
