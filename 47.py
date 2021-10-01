#Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.
import string

def find_message(message: str) -> str:
	res = ''

	for char in message:
		if char in string.ascii_uppercase:
			res += char
		else:
			continue

	return res

if __name__ == '__main__':
    print("Example:")
    print(find_message(('How are you? Eh, ok. Low or Lower? Ohhh.')))# == 'HELLO'
    print(find_message('hello world!'))# == ''
    print(find_message('HELLO WORLD!!!'))# == 'HELLOWORLD'