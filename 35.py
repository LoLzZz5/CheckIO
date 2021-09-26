#Ваша задача - переконвертировать время из 24-часового формата в 12-часовой.

hour = {'12' : '12',
		'13' : '1',
		'14' : '2',
		'15' : '3',
		'16' : '4',
		'17' : '5',
		'18' : '6',
		'19' : '7',
		'20' : '8',
		'21' : '9',
		'22' : '10',
		'23' : '11',
}

def time_converter(time):
    hours = int(time[:2])
    minutes = time[3:]

    if hours == 12 and int(minutes) == 0:
    	return str(hours) + ':' + minutes + ' p.m.'

    elif hours < 12 and hours != 0:
    	return str(hours) + ':' + minutes + ' a.m.'

    elif hours == 0:
    	return '12:' + minutes + ' a.m.'

    else:
    	if hours >= 12 and int(minutes) > 0:
    		return hour[str(hours)] + ':' + minutes + ' p.m.'

if __name__ == '__main__':
    print("Example:")
    print(time_converter('00:01'))# == '12:01 a.m.'
    print(time_converter('00:00'))# == '12:00 a.m.'
    print(time_converter('12:00'))# == '12:00 a.m.'
    print(time_converter('12:30'))# == '12:30 p.m.'
    print(time_converter('09:00'))# == '9:00 a.m.'
    print(time_converter('23:15'))# == '11:15 p.m.'