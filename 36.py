#Суммировать элементы списка по их типу
#На выходе сначала должна быть сумма элементов типа str, потом сумма элементов типа int
from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    intg = 0
    strn = ''

    for elem in items:
    	if type(elem) == int:
    		intg += elem
    	else:
    		strn += elem

    return (strn, intg)

if __name__ == "__main__":
    print("Example:")
    print(sum_by_types([]))# == ("", 0)
    print(sum_by_types([1, 2, 3]))# == ("", 6)
    print(sum_by_types(["1", 2, 3]))# == ("1", 5)
    print(sum_by_types(["1", "2", 3]))# == ("12", 3)
    print(sum_by_types(["1", "2", "3"]))# == ("123", 0)
    print(sum_by_types(["size", 12, "in", 45, 0]))# == ("sizein", 57)