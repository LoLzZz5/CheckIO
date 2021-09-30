#Реализовать вкл/выкл капс если в строке встречается символ "a"

def caps_lock(text: str) -> str:
    tmp = text.replace('a', '1')
    tmp = tmp.split('1')
    res = ''
    counter = 0

    for s in tmp:
        counter += 1
        if counter % 2 == 0:
            res += s.swapcase()
        else:
            res += s

    return res

if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))# == "Why RE YOU sking me thT?"
    print(caps_lock("Always wanted to visit Zambia."))# == "AlwYS Wnted to visit ZMBI."