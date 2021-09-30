# Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.

# Если в тексте две и больше буквы с одинаковой частотой , тогда результатом будет буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e"
import string

def checkio(text: str) -> str:
	text = text.replace(' ', '')
	text = text.lower()
	res = sorted(text)
	tmp = ''

	for i in res:
		tmp += i

	for i in (string.punctuation + string.digits):
		if i in tmp:
			tmp = tmp.replace(i, '')

	res = list(tmp)
	ch = res[0]
	mx = res.count(res[0])

	for char in res:
		if res.count(char) > mx:
			mx = res.count(char)
			ch = char
		else:
			continue

	return ch

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))# == "l", "Hello test"
    print(checkio("How do you do?"))# == "o", "O is most wanted"
    print(checkio("One"))# == "e", "All letter only once."
    print(checkio("Oops!"))# == "o", "Don't forget about lower case."
    print(checkio("AAaooo!!!!"))# == "a", "Only letters."
    print(checkio("abe"))# == "a", "The First."