# Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
# Люди предпочитают видеть эту же информацию в более развернутом виде: 21 May 2018 year, 16 hours 30 minutes
# Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.

def date_time(time: str) -> str:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    if time[0] != '0':
    	day = time[:2]
    else:
    	day = time[1]

    if time[3] != '0':
    	month = int(time[3:5])
    else:
    	month = int(time[4])

    if time[11] != '0':
    	hours = time[11:13]
    else:
    	hours = time[12]

    if len(hours) == 1 and hours == '0':
    	hours += ' hours '
    elif len(hours) == 1 and hours == '1':
    	hours += ' hour '
    else:
    	hours += ' hours '

    if time[14] != '0':
    	minutes = time[time.index(':') + 1:]
    else:
    	minutes = time[-1]

    if len(minutes) == 1 and minutes == '0':
    	minutes += ' minutes'
    elif len(minutes) == 1 and minutes == '1':
    	minutes += ' minute'
    else:
    	minutes += ' minutes'

    return day + ' ' + months[month - 1] + ' ' + time[6:time.index(' ') + 1] + 'year ' + hours + minutes


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))# == "1 January 2000 year 0 hours 0 minutes"
    print(date_time("09.05.1945 06:30"))# == "9 May 1945 year 6 hours 30 minutes"
    print(date_time("20.11.1990 03:55"))# == "20 November 1990 year 3 hours 55 minutes"