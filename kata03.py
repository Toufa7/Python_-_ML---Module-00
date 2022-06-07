phrase = "The right format"

c = '-'
i = 0
while (i < 25):
	print (c, end="")
	i += 1
	if (i == 25):
		print (phrase.format())

# The end=”” is used to print on same line without space.
# Keeping the doube quotes empty merge all the elements together in the same line.