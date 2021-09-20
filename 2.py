#Проверить все ли символы в строке являются заглавными.
#Если строка пустая или в ней нет букв - функция должна вернуть True.
def is_all_upper(text: str) -> bool:
    text=text.replace(' ','')
    if len(text)==0:
        return True
    elif text.isdigit()==True:
        return True
    elif text.isupper()==True:
        return True
    else:
        return False

if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))