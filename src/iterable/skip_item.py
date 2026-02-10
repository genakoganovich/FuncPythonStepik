def skip_item(words, n):
    it = iter(words)
    for _ in range(n):
        next(it)
    return next(it)


def read_input():
    words = input().split()
    n = int(input())
    return words, n


def main():
    words, n = read_input()
    print(skip_item(words, n))


if __name__ == "__main__":
    main()
