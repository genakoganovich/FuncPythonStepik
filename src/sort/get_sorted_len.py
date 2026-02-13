import re

def parse_string(s):
    return map(
        lambda m: m.group(),
        re.finditer(r'\S+', s)
    )


def get_sorted_len(s):
    return sorted(parse_string(s), key=len)


def read_input():
    return input()


def main():
    s = read_input()
    print(get_sorted_len(s))


if __name__ == "__main__":
    main()
