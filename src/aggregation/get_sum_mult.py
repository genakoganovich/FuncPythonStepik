import math

def get_sum_mult(sales_lines):
    return sum(math.prod(map(int, s.split())) for s in sales_lines)


def read_input():
    n = int(input())
    return [input() for _ in range(n)]


def main():
    sales_lines = read_input()
    print(get_sum_mult(sales_lines))


if __name__ == "__main__":
    main()
