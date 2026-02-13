import re


def enumerate_even_position(s):
    words_it = map(
        lambda m: m.group(),
        re.finditer(r'\S+', s)
    )
    words_even_pos_it = filter(
        lambda w: w[0] % 2 == 0,
        enumerate(words_it)
    )
    return "\n".join(f"{w}" for _, w in words_even_pos_it)

def read_input():
    return input()


def main():
    s = read_input()
    print(enumerate_even_position(s))

if __name__ == "__main__":
    main()
