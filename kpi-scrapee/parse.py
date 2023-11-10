
def parse(text, flag, endFlag):
	scraped = text
	flagLen = len(flag)
	endFlagLen = len(endFlag)
	parsing = True
	retString = ""
	idx=0
	length = len(scraped)
	#print(flag)
	#print(endFlag)
	#print(flagLen)
	while(parsing):
		#print(scraped[idx:idx+flagLen])
		#print(parsing)
		if scraped[idx:idx+flagLen] == flag and parsing:
			idx1 = idx
			for letter1 in scraped[idx+flagLen:idx+flagLen+120]:
				if scraped[idx1:idx1+endFlagLen] != endFlag:
					retString += letter1
					idx1= idx1+ 1
				if scraped[idx1:idx1+endFlagLen] == endFlag:
					parsing = False
		idx = idx + 1
	finalRet = retString[:-endFlagLen-3]
	print(finalRet)
	return finalRet
