import re


def filter_palindrome(s):
    words_it = map(
        lambda m: m.group(),
        re.finditer(r'\S+', s)
    )
    return list(filter(
        lambda word: word == word[::-1],
        words_it
    ))


def read_input():
    return input()


def main():
    s = read_input()
    print(filter_palindrome(s))

if __name__ == "__main__":
    main()
