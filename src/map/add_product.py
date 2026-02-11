import re

def add_product(s):
    return list(map(
        lambda m: f"product: {m.group()}",
         re.finditer(r'[^,\s]+', s)
    ))


def read_input():
    return input()


def main():
    s = read_input()
    print(add_product(s))

if __name__ == "__main__":
    main()
