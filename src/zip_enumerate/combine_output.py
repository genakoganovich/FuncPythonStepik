import re

def parse_csv(s):
    return map(
        lambda m: m.group(0),
        re.finditer(r'[^,]+?(?=[,]|$)', s)
    )

def combine_output(s, t):
    s_it = parse_csv(s)
    t_it = parse_csv(t)
    enum_it = enumerate(zip(s_it, t_it), start=1)
    combined_it = map(lambda x: f"{x[0]}. {x[1][0]} - {x[1][1]}", enum_it)
    return '\n'.join(combined_it)

def read_input():
    s = input()
    t = input()
    return s, t


def main():
    s, t = read_input()
    print(combine_output(s, t))

if __name__ == "__main__":
    main()
