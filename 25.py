# Вам предоставляется набор координат, в которых расставлены белые пешки. Вы должны подсчитать количество защищенных пешек.

def safe_pawns(pawns: set) -> int:
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))# == 6
    print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))# == 1