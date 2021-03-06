# Дан непустой массив целых чисел (X). В этой задаче вам нужно вернуть массив, состоящий только из неуникальных элементов данного массива. 
# Для этого необходимо удалить все уникальные элементы (которые присутствуют в данном массиве только один раз). Для решения этой задачи не меняйте оригинальный порядок элементов.

def checkio(data: list) -> list:
	res = []
	for i in data:
		if data.count(i) > 1:
			res.insert(0,i)
	res = res[::-1]
	return res

if __name__ == "__main__":
    print(list(checkio([1, 2, 3, 1, 3]))) #== [1, 3, 1, 3]
    print(list(checkio([1, 2, 3, 4, 5]))) #== []
    print(list(checkio([5, 5, 5, 5, 5]))) #== [5, 5, 5, 5, 5]
    print(list(checkio([10, 9, 10, 10, 9, 8]))) #== [10, 9, 10, 10, 9]