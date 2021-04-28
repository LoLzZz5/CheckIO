#Дана строка и нужно найти ее первое слово.
def first_word(text: str) -> str:
	result=''
	p=list(text)
	for i in p[:]:
		if i != ',' and i!=' 'and i!='.':
			break
		else:
			p.remove(i)
	for i in p:
		if i != ',' and i!=' 'and i!='.':
			result+=i
		else:
			break
	return result


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))#== "Hello"
    print(first_word(" a word "))# == "a"
    print(first_word("don't touch it"))# == "don't"
    print(first_word("greetings, friends"))# == "greetings"
    print(first_word("... and so on ..."))# == "and"
    print(first_word("hi"))# == "hi"
    print(first_word("Hello.World"))# == "Hello"