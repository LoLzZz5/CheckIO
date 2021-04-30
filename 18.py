#Перевернуть каждое слово в строке
def backward_string_by_word(text: str) -> str:
	dash=[]
	succ=''
	char=''
	if len(text)==0:
		return text
	else:
		dash =text.split(' ')
		for item in dash:
			succ+=item[::-1]
			succ+=' '
	return succ[0:len(succ)-1]

if __name__ == '__main__':
	print("Example:")
	print(backward_string_by_word(''))
	print(backward_string_by_word('world'))# == 'dlrow'
	print(backward_string_by_word('hello world'))# == 'olleh dlrow'
	print(backward_string_by_word('hello   world'))# == 'olleh   dlrow'
	print(backward_string_by_word('welcome to a game'))# == 'emoclew ot a emag'