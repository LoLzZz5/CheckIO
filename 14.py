#Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми.
#В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова.
def left_join(phrases: tuple) -> str:
	text=''
	text=','.join(phrases)
	text=text.replace('right','left')
	return text

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))# == "left,left,left,stop", "All to left"
    print(left_join(("bright aright", "ok")))# == "bleft aleft,ok", "Bright Left"
    print(left_join(("brightness wright",)))# == "bleftness wleft", "One phrase"
    print(left_join(("enough", "jokes")))# == "enough,jokes", "Nothing to replace"