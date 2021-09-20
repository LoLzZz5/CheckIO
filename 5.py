#Разделите строку на пары из двух символов. 
#Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').
def split_pairs(a):
	a1=''
	a2=''
	x=0
	result=[]
	if len(a)==1:
		a+='_'
		a=''.join(a)
		result.append(a)
	elif len(a)==0:
		return a
	else:
		for i in range(len(a)):
			a1+=a[i]
			x+=1
			if x ==2:
				result.append(a1)
				a1=''
				x=0
			if i==len(a)-1:
				if a1!='':
					result.append(a1)
	for elem in result:
		if len(elem)==1:
			a2+=elem
			result.remove(elem)
			a2+='_'
			result.append(a2)
	return result

if __name__ == '__main__':
	print("Example:")
	print(list(split_pairs('a')))
	print(list(split_pairs('abcd')))
	print(list(split_pairs('abc')))