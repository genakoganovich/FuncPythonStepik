import re


def filter_none(s):
    words_it = map(
        lambda m: m.group(0),
        re.finditer(r'[^,]+?(?=[,]|$)', s)
    )
    return list(filter(None, words_it))


def read_input():
    return input()


def main():
    s = read_input()
    print(filter_none(s))

if __name__ == "__main__":
    main()
