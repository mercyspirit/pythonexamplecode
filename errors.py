

try:
	2 + "henlo"
except TypeError:
	print("There was a type error")
finally:
	print("This was printed")

try:
	f = open('testfile.txt','r')
	f.write('Test write this')
except:
	print("Error in writing to the file")
finally:
	print("Always execute finally code blocks")


def askint():
	try:
		val = int(raw_input('Please enter an integer'))
	except:
		print("Looks like you didn't enter an integer")
		val = int(raw_input('Please enter an integer'))
	finally:
		print("Finally block executed")
print(val)	

askint()