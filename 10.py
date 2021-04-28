#Проверить является ли число четным или нет.
#Ваша функция должна возвращать True если число четное, и False если число не четное.
def is_even(num: int) -> bool:
    if num%2==0:
    	return True
    else:
    	return False


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))