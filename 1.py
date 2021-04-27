#удалить из спика все перед нужным элементов
from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    if border not in items:
        return items
    else:
        items=items[items.index(border)::]
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
    # print(list(remove_all_before([1, 1, 2, 2, 3, 3], 2)))
    # print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
    # print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
    # print(list(remove_all_before([1, 1, 5, 6, 7], 2)))
    # print(list(remove_all_before([10,1,5,6,7,10],5)))