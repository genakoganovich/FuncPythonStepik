import re


def parse_string_to_ints(s):
    return map(
        lambda m: int(m.group()),
        re.finditer(r'\S+', s)
    )


def sum_mult(s, t):
    s_it = parse_string_to_ints(s)
    t_it = parse_string_to_ints(t)
    return sum(map(lambda x, y: x * y, s_it, t_it))

def read_input():
    s = input()
    t = input()
    return s, t


def main():
    s, t = read_input()
    print(sum_mult(s, t))

if __name__ == "__main__":
    main()
