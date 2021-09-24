# Отсортируйте данный итератор таким образом, чтобы его элементы оказались в порядке убывания частоты их появления, то есть по количеству раз, которое они появляются в элементах.
# Если два элемента имеют одинаковую частоту, они должны оказаться в том же порядке, в котором стояли изначально в итераторе.
import operator

def frequency_sort(items):
    unique = []

    for elem in items: #создание списка с уникальными числами для подсчета кол-ва вхождений чисел
        if elem not in unique:
            unique.insert(0, elem)

    unique = unique[::-1]
    tmp = []

    for elem in unique: #создание словаря для хранения числа и его кол-ва вхождений
        unique1 = {}
        unique1['name'] = elem
        unique1['count'] = items.count(elem)
        tmp.insert(0, unique1)

    tmp = tmp[::-1]
    tmp = sorted(tmp, key = operator.itemgetter('count'), reverse = True) #сортировка по кол-ву вхождений
    res = []

    for elem in tmp: #создание списка для записи чисел по их кол-ву вхождений
        i = 0
        while i < elem['count']:
            res.insert(0, elem['name'])
            i += 1

    return res[::-1]


if __name__ == '__main__':
    print("Example:")
    print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))# == [4, 4, 4, 4, 6, 6, 2, 2]
    print(list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])))# == ['bob', 'bob', 'bob', 'carl', 'alex']
    print(list(frequency_sort([17, 99, 42])))# == [17, 99, 42]
    print(list(frequency_sort([])))# == []
    print(list(frequency_sort([1])))# == [1]