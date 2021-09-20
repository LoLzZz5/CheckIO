# Отсортируйте данный итератор таким образом, чтобы его элементы оказались в порядке убывания частоты их появления, то есть по количеству раз, которое они появляются в элементах.
# Если два элемента имеют одинаковую частоту, они должны оказаться в том же порядке, в котором стояли изначально в итераторе.
import operator

def frequency_sort(items):
	items.sort(items, key = operator.itemgetter(items))
	return items


if __name__ == '__main__':
    print("Example:")
    print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))# == [4, 4, 4, 4, 6, 6, 2, 2]
    print(list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])))# == ['bob', 'bob', 'bob', 'carl', 'alex']
    print(list(frequency_sort([17, 99, 42])))# == [17, 99, 42]
    print(list(frequency_sort([])))# == []
    print(list(frequency_sort([1])))# == [1]