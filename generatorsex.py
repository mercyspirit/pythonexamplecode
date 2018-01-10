def gencubes(n):
	out = []
	for num in range(n):
		out.append(num**3)
	return out

def genfibon(n):
	a = 1
	b = 1

	for i in range(n):
		yield a
		a,b = b, a + b

def fibon(n):
	a = 1
	b = 1

	output = []

	for i in range(n):
		output.append(a)
		a,b = b, a + b
	return output

def simple_gen():
	for x in range(3):
		yield x

print(gencubes(10))

for num in genfibon(10):
	print(num)

print(fibon(10))

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))

s_iter = iter(s)

print(s_iter)