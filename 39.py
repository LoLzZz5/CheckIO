#Найти координаты конечной точки. Буква «f» - указывает на то, что Вам нужно двигаться вперед, «b» - назад, «l» - влево, а «r» - вправо.
from typing import Tuple

def follow(instructions: str) -> Tuple[int, int]:
	f = 0
	lr = 0

	for char in instructions:
		if char == 'f':
			f += 1
		elif char == 'b':
			f -= 1
		elif char == 'l':
			lr -= 1
		else:
			lr += 1

	return (lr, f)

if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))# == (-1, 4)
    print(follow("ffrff"))# == (1, 4)
    print(follow("fblr"))# == (0, 0)