# Дан текст с разными словами и/или числами, которые разделены пробелами и знаками пунктуации. 
# Числа не считаются за слова (также как и смесь букв и цифр). Необходимо подсчитать слова, в которых гласные буквы чередуются с согласными.
# Слова состоящие из одной буквы - не "полосатые" (не считайте их). Регистр букв не имеет значения
import string

def checkio(line: str) -> str:
    counter = 0
    line = line.lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    if line.isdigit() == True:
    	return counter
    else:
	    for i in string.punctuation:
	        if i in line:
	            line = line.replace(i, ' ')

	    for i in vowels:
	        if i in line:
	            line = line.replace(i, '.')

	    for i in string.ascii_lowercase:
	        if i in line:
	            line = line.replace(i, '!')

	    line = line.split()

	    for word in line:
	        tmp = 0
	        if len(word) == 1:
	            continue
	        else:
	            for i in range(len(word)):
	                if i == len(word) - 1:
	                    tmp += 1
	                    continue
	                elif word[i] != word[i + 1] and word[i] not in string.digits:
	                    tmp += 1
	            if tmp == len(word):
	                counter += 1

	    return counter

if __name__ == '__main__':
    print("Example:")
    print(checkio('My name is ...'))# == 3
    print(checkio('Hello world'))# == 0
    print(checkio('A quantity of striped words.'))# == 1
    print(checkio('Dog,cat,mouse,bird.Human.'))# == 3
    print(checkio("1st 2a ab3er root rate"))# == 1