import re
import sys


def parse_string_it(s):
    return re.finditer(r'\S+', s)


def cast_to_int(it):
    return map(
        lambda m: int(m.group()),
        it
    )


def get_total_cost(s, t):
    return list(map(
        lambda m, n: m * n,
        cast_to_int(parse_string_it(s)),
        cast_to_int(parse_string_it(t))
    ))


def read_input():
    return [input() for _ in range(2)]


def main():
    s, t = read_input()
    print(get_total_cost(s, t))


if __name__ == "__main__":
    main()
