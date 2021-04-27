#В данном списке первый элемент должен стать последним.
#Пустой список или список из одного элемента не должен измениться.
from typing import Iterable


def replace_first(items: list) -> Iterable:
    if len(items)==1 or len(items)==0:
    	return items
    else:
    	items=items[1::]+items[0:1]
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))
    print(list(replace_first([1])))
    print(list(replace_first([])))
