def get_remains(words, k):
    it = iter(words)
    for _ in range(k):
        next(it)
    return "\n".join(it)


def read_input():
    words = input().split()
    k = int(input())
    return words, k


def main():
    words, k = read_input()
    print(get_remains(words, k))


if __name__ == "__main__":
    main()
