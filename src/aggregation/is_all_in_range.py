import re


def parse_string(s):
    return map(
        lambda m: int(m.group()),
        re.finditer(r'\S+', s)
    )

def is_all_in_range(s, lower_bound, upper_bound):
    return all(lower_bound <= n <= upper_bound for n in parse_string(s))


def read_input():
    return input()


def main():
    s = read_input()
    print(is_all_in_range(s, 0, 100))

if __name__ == "__main__":
    main()
