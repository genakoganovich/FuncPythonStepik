def get_sort_key(s):
    name, num = s.split()
    return -int(num), name


def get_sorted_tuple(s_lines):
    return "\n".join(sorted(
        s_lines,
        key=lambda x: get_sort_key(x)
    ))


def read_input():
    n = int(input())
    return [input() for _ in range(n)]


def main():
    s_lines = read_input()
    print(get_sorted_tuple(s_lines))


if __name__ == "__main__":
    main()
