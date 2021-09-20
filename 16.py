#У вас есть две даты в кортежах с тремя числами - год, месяц и день.
#Вы должны найти разницу в днях между имеющимися датами.
from datetime import date, timedelta
def days_diff(a, b):
	p = date(a[0],a[1],a[2])
	q = date(b[0],b[1],b[2])
	return abs((p - q).days)

if __name__ == '__main__':
	print("Example:")
	print(days_diff((1982, 4, 19), (1982, 4, 22)))
	print(days_diff((2014, 1, 1), (2014, 8, 27)))# == 238
	print(days_diff((2014, 8, 27), (2014, 1, 1)))# == 238