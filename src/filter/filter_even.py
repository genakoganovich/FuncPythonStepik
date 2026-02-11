import re

def filter_even(s):
    int_it = map(
        lambda m: int(m.group()),
        re.finditer(r'\S+', s)
    )
    return list(filter(
        lambda m: m % 2 == 0,
        int_it
    ))


def read_input():
    return input()


def main():
    s = read_input()
    print(filter_even(s))


if __name__ == "__main__":
    main()
