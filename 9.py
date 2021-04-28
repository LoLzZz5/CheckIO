#На вход Вашей функции будет передано одно предложение.
#Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
def correct_sentence(text: str) -> str:
	result=''
	result+=text[0].title()
	result+=text[1:]
	if result[len(result)-1]!='.':
		result+='.'
	return result


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    print(correct_sentence("Greetings, friends"))# == "Greetings, friends."
    print(correct_sentence("Greetings, friends."))# == "Greetings, friends."
    print(correct_sentence("hi"))#== "Hi."
    print(correct_sentence("welcome to New York"))#== "Welcome to New York."