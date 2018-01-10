def ask():
	while True:
		try:
			val = int(input("Input an integer: "))
		except:
			print("An error occurred. Try again")
			continue
		else:
			print("Thank you, the number squared is %d" % val**(2))
			break


try:
	for i in ['a','b','c']:
		print(i**2)
except TypeError:
	print("Array type does not match")


try:
	x = 5
	y = 0
	z = x/y
except ZeroDivisionError:
	print("Can't divide by zero!!!")
finally:
	print("All done")

ask()