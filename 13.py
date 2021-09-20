#Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
#Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
def checkio(text: str) -> bool:
	text=text.lower()
	text =text.split()
	lcounter=0
	dcounter=0
	for item in text:
		if lcounter>=3:
			continue
		for i in item:
			for l in range(97,123):
				if i == chr(l):
					lcounter+=1
					break
			for n in range(48,58):
				if i == chr(n):
					dcounter+=1
					lcounter=0
					break
			break
	if lcounter>=3:
		return True
	else:
		return False

if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    print(checkio("He is 123 man"))# == False, "123 man"
    print(checkio("bla bla bla bla"))# == True, "Bla Bla"
    print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))