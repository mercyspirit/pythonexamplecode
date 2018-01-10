def fahrenheit(T):
	return (9.0/5)*T + 32

print(fahrenheit(0))

temp = [0,22.5,40,100]

l = map(fahrenheit, temp)

for i in l:
	print(i)

for i in (map(lambda T: (9.0/5)*T + 32, temp)):
	print(i)

lambda x,y: x + y

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

for i in (map(lambda x,y,z: x+y+z,a,b,c)):
	print(i)

for i in (map(lambda num: num*-1, a)):
	print(i)