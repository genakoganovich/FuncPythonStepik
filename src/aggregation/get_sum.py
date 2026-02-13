import re


def parse_string(s):
    return map(
        lambda m: int(m.group()),
        re.finditer(r'\S+', s)
    )


def get_sum(s):
    return sum(parse_string(s))


def read_input():
    return input()


def main():
    s = read_input()
    print(get_sum(s))


if __name__ == "__main__":
    main()
