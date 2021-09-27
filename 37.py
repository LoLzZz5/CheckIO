# Птичка меняет слова по следующим правилам:
# - после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
# - после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa);
# Гласные буквы == "aeiouy".
# Вам дана птичья фраза как несколько слов, разделёных пробелами (каждая пара слов разделена одним пробелом). Преобразуйте птичий язык.

def translate(text: str) -> str:
	vowels = ['a', 'e', 'i', 'o', 'u', 'y']
	tmp = list(text)
	res = ''

	for index in range(len(tmp)):
		if tmp[index] == '1':
			continue
		else:
			if tmp[index] not in vowels and tmp[index] != ' ' and tmp[index + 1] in vowels:
				del tmp[index + 1]
				tmp.insert(index + 1, '1')

	for char in tmp:
		if char != '1':
			res += char

	for vowel in vowels:
		res = res.replace(vowel * 3, vowel)

	return res

if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))# == "hello"
    print(translate("hoooowe yyyooouuu duoooiiine"))# == "how you doin"
    print(translate("aaa bo cy da eee fe"))# == "a b c d e f"
    print(translate("sooooso aaaaaaaaa"))# == "sos aaa"