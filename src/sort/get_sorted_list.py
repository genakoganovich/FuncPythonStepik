import re

def parse_string(s):
    return map(
        lambda m: m.group(),
        re.finditer(r'\S+', s)
    )


def get_sorted_list(s):
    return sorted(int(x) for x in parse_string(s))


def read_input():
    return input()


def main():
    s = read_input()
    print(get_sorted_list(s))


if __name__ == "__main__":
    main()
