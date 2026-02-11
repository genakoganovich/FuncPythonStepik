import re


def get_len(s):
    gen = (m.group() for m in re.finditer(r'\S+', s))
    for word in gen:
        yield len(word)


def read_input():
    return input()


def main():
    s = read_input()
    print(list(get_len(s)))


if __name__ == "__main__":
    main()
