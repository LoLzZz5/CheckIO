#Определить угол солнца над горизонтом, зная время суток. 
#Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов. В 12:00 солнце в зените, а значит угол = 90 градусов. В 18:00 солнце садится за горизонт и угол равен 180 градусов. 
#В случае, если указано ночное время (раньше 6:00 или позже 18:00), функция должна вернуть фразу "I don't see the sun!".
from typing import Union

def sun_angle(time: str) -> Union[int, str]:
    hour = time[:2]
    minute = time[3:]
    res = 0

    if hour[0] == '0':
    	hour = int(hour[1])
    else:
    	hour = int(hour)

    if minute[0] == '0':
    	minute = int(minute[1])
    else:
    	minute = int(minute) 

    if hour > 6 and hour < 18 :
    	return (hour - 6) * 15 + minute * 0.25

    else:
    	return "I don't see the sun!"
  
if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))# == 15
    print(sun_angle("01:23"))# == "I don't see the sun!"