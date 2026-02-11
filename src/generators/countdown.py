def countdown(n):
    for i in range(n, 0, -1):
        yield i


def read_input():
    return 0


def main():
    for number in countdown(5):
        print(number)


if __name__ == "__main__":
    main()
