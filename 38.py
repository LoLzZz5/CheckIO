#Найти похожие слова в 2-х строчках. Выход должен быть в алфавитном порядке.

def checkio(line1: str, line2: str) -> str:
    res = ''
    tmp1, tmp2 = line1.split(','), line2.split(',')
    tmp = []

    for word in tmp1:
    	if tmp2.count(word) > 0:
    		tmp.insert(0, word)

    tmp = sorted(tmp)

    for word in tmp:
    	res += word + ','

    return res[:res.rfind(',')]


if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))# == 'hello'
    print(checkio('one,two,three', 'four,five,six'))# == ''
    print(checkio('one,two,three','four,five,one,two,six,three'))# == 'one,three,two'
    print(checkio("mega,cloud,two,website,final","window,penguin,literature,network,fun,cloud,final,sausage"))