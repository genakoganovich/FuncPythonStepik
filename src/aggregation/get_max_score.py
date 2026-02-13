def get_max_score(students):
    return max(students, key=lambda x: x['score'])['name']


def read_input():
    n = int(input())
    students = []
    for _ in range(n):
        name, score = input().split()
        students.append({'name': name, 'score': int(score)})

    return students


def main():
    students = read_input()
    print(get_max_score(students))


if __name__ == "__main__":
    main()
