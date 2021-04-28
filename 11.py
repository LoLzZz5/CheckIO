#Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом.
#Если число является частью слова, то его суммировать не нужно.
def sum_numbers(text: str) -> int:
	text =text.split()
	for item in text[:]:
		dcounter=0
		tcounter=0
		lcounter=0
		for i in item:
			for t in range(65,91):
				if i == chr(t):
					tcounter+=1
			for l in range(97,123):
				if i == chr(l):
					lcounter+=1
			for n in range(48,58):
				if i == chr(n):
					dcounter+=1
		if tcounter > 0:
			text.remove(item)
		elif lcounter >0:
			text.remove(item)
	text=[int(item) for item in text]
	return sum(text)

if __name__ == '__main__':
	print("Example:")
	print(sum_numbers('Petersen between 1845 and 1910 year')) #== 3755
	print(sum_numbers('5 plus 6 is'))