import re


def enumerate_tasks(s):
    tasks_it = map(
        lambda m: m.group(0),
        re.finditer(r'[^,]+?(?=[,]|$)', s)
    )
    return "\n".join(f"{i}. {task}" for i, task in enumerate(tasks_it, start=1))


def read_input():
    return input()


def main():
    s = read_input()
    print(enumerate_tasks(s))

if __name__ == "__main__":
    main()
