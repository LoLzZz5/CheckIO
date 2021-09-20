#Вам дана строка и два маркера (начальный и конечный).
#Вам необходимо найти текст, заключенный между двумя этими маркерами.
def between_markers(text: str, begin: str, end: str) -> str:
	return text[text.index(begin)+1:text.index(end)]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    print(between_markers('What is [apple]', '[', ']'))# == "apple"
    print(between_markers('What is ><', '>', '<'))# == ""
    print(between_markers('>apple<', '>', '<'))#== "apple"