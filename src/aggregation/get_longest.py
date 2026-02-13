import re

def parse_string(s):
    return map(
        lambda m: m.group(),
        re.finditer(r'\S+', s)
    )

def get_longest(s):
    return max(parse_string(s), key=len)


def read_input():
    return input()


def main():
    s = read_input()
    print(get_longest(s))


if __name__ == "__main__":
    main()
