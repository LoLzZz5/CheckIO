#Посчитать кол-во цивф в стоке
def count_digits(text: str) -> int:
	dcounter=0
	for i in text:
		for j in range(48,58):
			if i == chr(j):
				dcounter+=1
	return dcounter

if __name__ == '__main__':
	print("Example:")
	print(count_digits('hi'))# == 0
	print(count_digits('who is 1st here'))# == 1
	print(count_digits('my numbers is 2'))# == 1