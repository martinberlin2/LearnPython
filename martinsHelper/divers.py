

# divers.py   TODO Headers, nach only_sig_from_module
# hier sind Funktionen drin, die auch ausserhalb der Katas gebraucht werden könnten

# import logging  # für Debugausgaben noch drin

def getCharFromStringByPos(s, pos): #-> char oder None (bei IndexError)
	if pos > len(s)-1 or pos < 0:
		return None
	return s[pos]

def isWordSeparator(char): #-> True wenn char == None, Tab or Space
	if char in [None, "	", " "]: # TAB, Blank
		return True
	return False

def containsString(strg, substr, asWord): # -> pos of first char found or False. EmptyString -> "containsString:EmptyString", asWord: before and after TAB- or space- separated
	if strg == '' or substr == '':
		return "containsString:EmptyString"
	# foundpos = False
	pos = 0
	endpos = len(strg) - len(substr)
	while pos <= endpos :
		if strg[pos] == substr[0]:
			if strg[pos : pos + len(substr)] == substr:
				if asWord == False:
					return pos
				else: 
					charBefore = getCharFromStringByPos(strg, pos-1)
					# logging.info("charBefore", str, pos-1, "!", charBefore, "!")
					charAfter  = getCharFromStringByPos(strg, pos + len(substr))
					# logging.info("charAfter", str, len(substr)+1, "!", charAfter, "!")
					if isWordSeparator(charBefore) and isWordSeparator(charAfter):
						return pos
		pos = pos + 1
	return "containsString:False"

def addLeadingZeros(num, digits): # --> String for logging.info. num ist integer.
	s = str(num)
	minus = ""
	if s[0] == "-":
		s = s[1:]
		minus = "-"
	while len(s) < digits:
		s = '0' + s
	s = minus + s
	return s
	
def NumberFromString(s): # -> float and int, otherwise "NaN". TODO complex, long
	try:
		ints = int(s)
		return ints
	except ValueError as VError:
		try:
			floats = float(s)
			return floats
		except ValueError as VError2:
			return "NaN"

def getElem(node): # INTERN für listStringToList - "5" -> 5, "'x'" -> 'x' ; führende Blanks weg. Kein realElem: wirft Exceptions 'start quote missing', 'end quote missing'
	realElem = node.strip()
	# logging.info ("realElem:", realElem, "!", len(realElem))
	mynum = NumberFromString(realElem)
	if mynum != "NaN":
		# logging.info("return realElem Zahl", mynum , len(realElem))
		return mynum
	if realElem[0] != '"' and realElem[0] != "'":
		raise Exception('start quote missing') # as NotValidElem		
		return(node)
	if realElem[-1] != realElem[0]:
		raise Exception('end quote missing') # as NotValidElem
		return(node)
	realElem = realElem[1:-1]
	# logging.info("return realElem String", realElem, len(realElem))
	return realElem	

def listStringToList(listString): # --> [List - Dimension je nach String, errString]
	listString = str(listString)  # falls einzelne Zahl kommt [3.5] 
	# logging.info('--Rekursion mit listString; Strip folgt:' + listString + '!' + str(len(listString)))
	listString = listString.strip()
	result = []
	errString = ""
	if len(listString) < 2:
		errString = "kein ListString, zu kurz fuer []"	
		return [result, errString]
	if listString[0] != "[" or listString[-1] != "]":
		# logging.info ("listString[0]=", listString[0])
		# logging.info ("listString[-1]=", listString[-1])
		errString = "kein ListString '[s]'; s = String: [] aussen fehlen"
		return [result, errString] # hier ohne Exception gelöst
	Ls = listString[1:-1]  # Aussenklammern sind geprüft, jetzt Aufzählung von Elem erwartet
	
	# logging.info("Ls nach [] Check:                        ", Ls, '!')
	ko = 0 # Klammern Offen, Zähler
	node = "" # String ist wieder ListString, Element, oder Syntaxfehler 
	pos = -1
	while pos < len(Ls)-1:
		pos = pos + 1
		# # logging.info ("pos ", pos)
		c = Ls[pos]
		# logging.info ("pos: ", pos, "Char: " , c)
		if c == "[": 
			ko = ko + 1
		if c == "]": 
			ko = ko - 1
		if ko < 0:
			errString = "Klammerfehler, Pos " + str(pos)
			return [result, errString]
		if pos == len(Ls)-1: # String zuende ersetzt Komma beim Erkennen von Node-Ende
			# logging.info ("LAST:", c, pos)
			node = node + c
			c = ","
		if c == "," and ko == 0: # erwarte hier einen Node - ListString oder Element
			errString = ""
			try:
				elem = getElem(node) # "5" -> 5, "'x'" -> 'x' ; führende Blanks weg. Kein realElem: wirft NotValidElem
				# logging.info("try durch, macht append elem:", elem)
				result.append(elem)
			except Exception as NotValidElem: 
				# logging.info(NotValidElem.args)
				# könnte ListString sein - mit neuen Aussenklammern; wenn nicht, Fehler
				outlist = listStringToList(node)   #
				resultHere = outlist[0]
				errString = outlist[1]
				if errString != "":
					# logging.info ("errString z 107: ", errString)
					return [[], "Quote Error"]
				result.append(resultHere)
			node = ""
			continue
		node = node + c
	if ko != 0:
		errString = "Klammerfehler hinten"
		result = []
	# logging.info ("result nach Rek.-Ende:" + str(result) + "Errors:" + errString + "!")
	# logging.info (str(len(errString)))
	# logging.info("ListString war:       ", listString)
	return [result, errString]

def sumOfDigits(number): # --> Quersumme, -1 wenn number kein int oder < 0. number nicht als String! --> -1 Truely oder Falsely geben 0 oder 1
	
	import logging
	# logging.info ("\nsumOfDigits!" + str(number) + "!")
	try:
		temp = number - 2
		# logging.info ("temp:" + str(temp) + "!")
	except TypeError as te:
		# logging.info ("temp:" + str(temp) + "TYPE ERROR")
		return -1
	try:
		x = int(number)
	except ValueError as ve:
		return -1
	except Exception as ex:
		return -2 # unexpected!
	# logging.info ("nach int number:" + str(x) + "!")
	if x < 0: return -1
	# if x != x / 1: return -1
	sum = 0
	while x > 0:
		rest = int(x % 10)
		x = int((x - rest) / 10)
		sum = sum + rest
	return sum 

def stringToWordList(s): # --> [strings] s wird nach Blanks getrennt, Blanks nur Trenner, auch für leere Wörter
	result = []
	aktStr = ""
	workStr = s
	pos = 0
	while pos < len(workStr):
		first = workStr[pos]
		if first == " ":
			result.append(aktStr)
			aktStr = ""
		else:
			aktStr = aktStr + first
		pos = pos + 1
	result.append(aktStr)	
	return result	

def wordlistToString(wordlist): # --> String, Wörter nach Blanks getrennt
	result = ""
	while len(wordlist) > 0:
		# print ("wordlist[0] = " + str(wordlist[0])) 
		result = result + wordlist[0] + " "
		wordlist = wordlist[1:len(wordlist)]
		# print ("wordlist = " + str(wordlist))
	result = result[0:len(result)-1]
	return result