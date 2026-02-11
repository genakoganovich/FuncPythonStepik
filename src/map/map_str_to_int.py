import re


def map_str_to_int_list(s):
    nums = list(map(
        lambda m: int(m.group()),
        re.finditer(r'\S+', s)
    ))
    return nums


def read_input():
    return input()


def main():
    s = read_input()
    print(map_str_to_int_list(s))


if __name__ == "__main__":
    main()
