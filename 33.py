#Проверить идут ли два символа один за другим.

def goes_after(word: str, first: str, second: str) -> bool:
    if first == second:
    	return False
    elif word.find(first) == -1 or word.find(second) == -1:
    	return False
    else:
    	if word.find(first) + 1 == word.find(second):
    		return True
    	else:
    		return False

if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))# == True
    print(goes_after('world', 'w', 'r'))# == False
    print(goes_after('world', 'l', 'o'))# == False
    print(goes_after('panorama', 'a', 'n'))# == True
    print(goes_after('list', 'l', 'o'))# == False
    print(goes_after('', 'l', 'o'))# == False
    print(goes_after('list', 'l', 'l'))# == False
    print(goes_after('world', 'd', 'w'))# == False