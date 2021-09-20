#У вас есть число и нужно определить какая цифра из этого числа является наибольшей.
def max_digit(number: int) -> int:
	s=str(number)
	n =list(s)
	result= [int(item) for item in n]
	result = max(result)
	return result


if __name__ == '__main__':
	print("Example:")
	print(max_digit(7523))
	# print(max_digit(0))
	# print(max_digit(52))
	# print(max_digit(634))
	# print(max_digit(1))
	# print(max_digit(10000))