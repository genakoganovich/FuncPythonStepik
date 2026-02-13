import re

def filter_range(s, lower_bound, upper_bound):
    int_it = map(
        lambda m: int(m.group()),
        re.finditer(r'\S+', s)
    )
    return list(filter(
        lambda m: lower_bound <= m <= upper_bound,
        int_it
    ))


def read_input():
    s = input()
    lower_bound = int(input())
    upper_bound = int(input())
    return s, lower_bound, upper_bound

def main():
    s, lower_bound, upper_bound = read_input()
    print(filter_range(s, lower_bound, upper_bound))

if __name__ == "__main__":
    main()
