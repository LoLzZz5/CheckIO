#Найти топ самых дорогих товаров. Кол-во товаров, которые мы ищем, будут задаваться первым аргументом
from pprint import pprint
import operator

def bigger_price(limit: int, data: list) -> list:
    q = []
    data = sorted(data, key = operator.itemgetter('price'), reverse = True)
    for i in range(0, limit):
        q.insert(0, data[i])
    q = q[::-1]
    return q


if __name__ == '__main__':
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))