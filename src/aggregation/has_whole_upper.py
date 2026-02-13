import re



def parse_string(s):
    return map(
        lambda m: m.group(),
        re.finditer(r'\S+', s)
    )


def has_whole_upper(s):
    return any(x.isupper() for x in parse_string(s))


def read_input():
    return input()


def main():
    s = read_input()
    print(has_whole_upper(s))


if __name__ == "__main__":
    main()
