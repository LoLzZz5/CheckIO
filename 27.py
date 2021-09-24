#Разделить один список на два. Первая часть списка должна быть больше второй, если список пустой, то вернуть два пустых списка

def split_list(items: list) -> list:
	res = []
	tmp0 = []
	tmp1 = []

	if len(items) % 2 == 0:
		tmp0 = items[:len(items)//2]
		tmp1 = items[len(items)//2:]
		res.insert(0, tmp1)
		res.insert(0, tmp0)

	else:
		tmp0 = items[:len(items)//2 + 1]
		tmp1 = items[len(items)//2 + 1:]
		res.insert(0, tmp1)
		res.insert(0, tmp0)

	return res

if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))# == [[1, 2, 3], [4, 5, 6]]
    print(split_list([1, 2, 3]))# == [[1, 2], [3]]
    print(split_list([1, 2, 3, 4, 5]))# == [[1, 2, 3], [4, 5]]
    print(split_list([1]))# == [[1], []]
    print(split_list([]))# == [[], []]