#Даны 2 строки. Необходимо найти индекс второго вхождения второй строки в первую.
def second_index(text: str, symbol: str) -> [int, None]:
    counter=0
    if text.count(symbol)>=2:
        for i in range(len(text)):
            if text[i] == symbol and counter==1:
                return i
                break
            elif text[i]== symbol:

                counter+=1
    else:
        return None

if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))# == 3, "First"
    print(second_index("find the river", "e"))# == 12, "Second"
    print(second_index("hi", " "))# is None, "Third"
    print(second_index("hi mayor", " "))# is None, "Fourth"
    print(second_index("hi mr Mayor", " "))# == 5, "Fifth"