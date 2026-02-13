def get_max_diff(s):
    nums = [int(x) for x in s.split()]
    return max(nums) - min(nums)


def read_input():
    return input()


def main():
    s = read_input()
    print(get_max_diff(s))


if __name__ == "__main__":
    main()
