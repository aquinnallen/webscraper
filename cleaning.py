import sys
file = sys.argv[1]


def clean(filename):
	with open(filename) as d:
		 data = d.read()
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

clean(file)
