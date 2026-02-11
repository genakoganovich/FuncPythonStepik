import random

def random_numbers(count, limit):
    for _ in range(count):
        yield random.randint(1, limit)


def read_input():
    return 0


def main():
    random.seed(42)  # Фиксируем случайность для предсказуемого результата
    print(list(random_numbers(5, 100)))



if __name__ == "__main__":
    main()
