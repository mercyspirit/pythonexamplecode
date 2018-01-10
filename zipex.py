x = [1,2,3]
y = [4,5,6]

for i in zip(x,y):
	print(i)

a = [1,2,3,4,5]
b = [2,2,10,1,1]

for pair in zip(a,b):
	print(max(pair))

l = map(lambda pair: max(pair), zip(a,b))

print(l)

x = [1,2,3]
y = [4,5,6,7]

print(zip(x,y))

d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}
def switcharoo(d1,d2):

	dout = {}

	for d1key,d2val in zip(d1,d2.itervalues()):
		dout[d1key] = d2val

	return dout

print(switcharoo(d1,d2))