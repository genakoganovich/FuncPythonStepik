import re


def sum_square_even(s):
    matches = re.finditer(r'\S+', s)
    ints_iter = map(lambda m: int(m.group()), matches)
    evens_iter = filter(lambda x: x % 2 == 0, ints_iter)
    return sum(map(lambda x: x ** 2, evens_iter))  # Даже map(**2)


def read_input():
    return input()


def main():
    s = read_input()
    print(sum_square_even(s))


if __name__ == "__main__":
    main()
