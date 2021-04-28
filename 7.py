#Найдите ближайшее значение к переданному.
def nearest_value(values: set, one: int) -> int:
	result=[]
    for i in values:
		result.append(i)
	result.sort()
	if max(result)<one:
		return max(result)
	elif min(result)>one:
		return min(result)
	elif one in result:
		return one
	else:
		for i in result:
			if i > one and i -one==1:
				return i
			elif i<one and i-one==-1:
				return i


if __name__ == '__main__':
	print("Example:")
	print(nearest_value({4, 7, 10, 11, 12, 17}, 9))#== 10
	print(nearest_value({4, 7, 10, 11, 12, 17}, 8))#== 7
	print(nearest_value({4, 8, 10, 11, 12, 17}, 9))#== 8
	print(nearest_value({-1, 2, 3}, 0))#== -1
	print(nearest_value({4, 7, 10, 11, 12, 17}, 100))#==17