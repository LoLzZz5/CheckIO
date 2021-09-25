#Отсортировать список по абсолютным значениям.

def checkio(values: list) -> list:
	tmp = []

	for elem in values:
		tmp.insert(0, abs(elem))

	tmp.sort()
	tmp0 = ''

	for elem in tmp:
		tmp0 += str(elem) + ' '

	for elem in values:
		tmp0 = tmp0.replace(str(abs(elem)), str(elem), 1)

	tmp0 = tmp0.rstrip(' ')
	tmp0 = tmp0.split()

	for elem in tmp0:
		tmp0 = [int(elem) for elem in tmp0]

	return tmp0


if __name__ == '__main__':
    print("Example:")
    print(checkio([-20, -5, 10, 15]))# == [-5, 10, 15, -20]
    print(checkio([1, 2, 3, 0]))# == [0, 1, 2, 3]
    print(checkio([-1, -2, -3, 0]))# == [0, -1, -2, -3]
