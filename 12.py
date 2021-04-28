#Дан массив целых чисел. 
#Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива.
def checkio(array: list) -> int:
	result=0
	if len(array)==0:
		return 0
	elif len(array)==1:
		result+=array[0]*array[0]
		return result
	else:
		result+=sum(array[0::2])
		result*=array[len(array)-1]
	return result

if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))# == 30, "(0+2+4)*5=30"
    print(checkio([1, 3, 5]))# == 30, "(1+5)*5=30"
    print(checkio([6]))# == 36, "(6)*6=36"
    print(checkio([]))# == 0, "An empty array = 0"