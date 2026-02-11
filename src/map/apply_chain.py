import re


def apply_chain(s):
    float_iter = map(
        lambda m: float(m.group()),
        re.finditer(r'\S+', s)
    )
    int_iter = map(
        lambda m: round(m),
        float_iter
    )
    return list(map(
        lambda m: str(m),
        int_iter
    ))


def read_input():
    return input()


def main():
    s = read_input()
    print(apply_chain(s))


if __name__ == "__main__":
    main()
