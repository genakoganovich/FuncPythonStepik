def powers_of_two(n):
    for i in range(n + 1):
        yield 1 << i


def read_input():
    return 0


def main():
    # Этот код не нужно отправлять в решение, он для проверки
    print(list(powers_of_two(4)))
    return 0


if __name__ == "__main__":
    main()
