#Надо определить, все ли элементы массива равны.
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    tmp = []

    for elem in elements:
    	if elem not in tmp:
    		tmp.insert(0, elem)

    if len(tmp) <= 1:
    	return True
    else:
    	return False

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))# == True
    print(all_the_same([1, 2, 1]))# == False
    print(all_the_same(['a', 'a', 'a']))# == True
    print(all_the_same([]))# == True
    print(all_the_same([1]))# == True