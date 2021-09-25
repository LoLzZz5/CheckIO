#Убрать все акценты в строке.
import unidecode

def checkio(in_string):
	return unidecode.unidecode(in_string)

if __name__ == '__main__':
    print(checkio(u"préfèrent"))# == u"preferent"
    print(checkio(u"loài trăn lớn"))# == u"loai tran lon"