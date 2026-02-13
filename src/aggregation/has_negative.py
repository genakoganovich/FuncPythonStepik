import re


def parse_string(s):
    return map(
        lambda m: int(m.group()),
        re.finditer(r'\S+', s)
    )


def has_negative(s):
    return any(x < 0 for x in parse_string(s))


def read_input():
    return input()


def main():
    s = read_input()
    print(has_negative(s))


if __name__ == "__main__":
    main()
