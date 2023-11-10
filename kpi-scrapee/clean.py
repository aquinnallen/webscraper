
def clean(text):
	data=text
	strings = data.split(";")
	outList = []
	#print(strings)
	for string in strings[0:-1]:
		split = string.split(":")
		outList.append(split[1])
	output = ",".join(outList)
	output = output +"\n"
	print(output)
	return output

