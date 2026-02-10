def iterate(words):
    it = iter(words)
    for w in it:
        print(w)

def read_input():
    return input().split()


def main():
    words = read_input()
    iterate(words)

if __name__ == "__main__":
    main()
