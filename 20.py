# Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий:
# Начальный и конечный маркеры всегда разные
	# Если нет начального маркера, то началом считать начало строки
	# Если нет конечного маркера, то концом считать конец строки
	# Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
	# Если конечный маркер стоит перед начальным, то вернуть пустую строку

def between_markers(text: str, begin: str, end: str) -> str:
	if text.find(end) == -1 and text.find(begin) == -1:
		return text
	elif text.find(begin) == -1:
		return text[:text.index(end)]
	elif text.find(end) == -1:
		return text[text.index(begin) + len(begin):]
	elif text.find(end) < text.find(begin):
		return ''
	else:
		return text[text.index(begin) + len(begin):text.index(end)]

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))# == "apple"
    print(between_markers("<head><title>My new site</title></head>", "<title>", "</title>"))# == "My new site"
    print(between_markers('No[/b] hi', '[b]', '[/b]'))# == 'No'
    print(between_markers('No [b]hi', '[b]', '[/b]'))# == 'hi'
    print(between_markers('No hi', '[b]', '[/b]'))# == 'No hi'
    print(between_markers('No <hi>', '>', '<'))# == ''