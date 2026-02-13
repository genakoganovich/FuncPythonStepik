import re


def parse_string(s):
    return map(
        lambda m: m.group(),
        re.finditer(r'\S+', s)
    )


def create_dict(s, t):
    return dict(zip(parse_string(s), parse_string(t)))


def read_input():
    s = input()
    t = input()
    return s, t


def main():
    s, t = read_input()
    print(create_dict(s, t))


if __name__ == "__main__":
    main()
