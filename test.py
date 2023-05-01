print('hello world')
print('this is a fibonnaci sequence implementation')

a,b = 0,1

for i in range(10):
	a,b = b,a+b
	print(b)
