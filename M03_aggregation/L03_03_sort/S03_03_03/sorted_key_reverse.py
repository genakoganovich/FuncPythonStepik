students = [
    {'name': 'Анна', 'score': 92},
    {'name': 'Борис', 'score': 58},
    {'name': 'Виктор', 'score': 75},
    {'name': 'Галина', 'score': 81}
]

# 1. С помощью key указываем, что сравнивать нужно по баллам.
# 2. С помощью reverse=True указываем, что порядок должен быть обратным.
leaderboard = sorted(students, key=lambda student: student['score'], reverse=True)

print("Лидерборд студентов:")
for student in leaderboard:
    print(student)