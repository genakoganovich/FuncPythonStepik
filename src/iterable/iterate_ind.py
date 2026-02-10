def iterate_ind(words):
    it_1 = iter(words)
    it_2 = iter(words)
    next(it_1)
    next(it_2)
    next(it_2)
    return next(it_1), next(it_2)


def read_input():
    return input().split()


def main():
    words = read_input()
    w_1, w_2 = iterate_ind(words)
    print(w_1)
    print(w_2)

if __name__ == "__main__":
    main()
