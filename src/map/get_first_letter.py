import re


def get_first_letter(s):
    return list(map(
        lambda m: m.group()[0].upper(),
        re.finditer(r'\S+', s)
    ))


def read_input():
    return input()


def main():
    s = read_input()
    print(get_first_letter(s))


if __name__ == "__main__":
    main()
