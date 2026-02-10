def get_first(words):
    return next(iter(words))


def read_input():
    return input().split()


def main():
    words = read_input()
    print(get_first(words))


if __name__ == "__main__":
    main()
