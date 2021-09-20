#Вам дана строка состоящая только из цифр.
#Вам нужно посчитать сколько нулей ("0") находится в начале строки

def beginning_zeros(number: str) -> int:
    counter=0
    for i in number:
        if i =='0':
            counter+=1
        else:
            break
    return counter


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))
    print(beginning_zeros('001'))
    print(beginning_zeros('100100'))
    print(beginning_zeros('001001'))
    print(beginning_zeros('012345679'))
    print(beginning_zeros('0000'))