import re

def filter_long_words(s):
    words_it = map(
        lambda m: m.group(),
        re.finditer(r'\S+', s)
    )
    return list(filter(
        lambda m: len(m) > 5,
        words_it
    ))


def read_input():
    return input()


def main():
    s = read_input()
    print(filter_long_words(s))


if __name__ == "__main__":
    main()
