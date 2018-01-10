while True:
	try:
		digit = int(input("Type in the number of digits you would like to see"))

	except TypeError:
		print("Input was not an integer, please try again.")
		continue
	else:
		print("%0." + str(digit) + "f" % (22/7))
		break