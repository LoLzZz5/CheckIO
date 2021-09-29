import string

def check_pangram(text):
    text = text.lower()
    text = text.replace(' ', '')

    for ch in string.punctuation:
        if ch in text:
            text = text.replace(ch, '')


    for char in string.ascii_lowercase:
        if text.find(char) == -1:
            return False
            break

    return True

if __name__ == '__main__':
    print(check_pangram("The quick brown fox jumps over the lazy dog."))
    print(check_pangram("ABCDEF"))
    print(check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"))