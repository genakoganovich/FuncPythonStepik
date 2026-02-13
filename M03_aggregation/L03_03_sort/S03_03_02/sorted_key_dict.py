students = [
    {'name': 'Анна', 'score': 92},
    {'name': 'Борис', 'score': 58},
    {'name': 'Виктор', 'score': 75},
    {'name': 'Галина', 'score': 81}
]

# Для каждого словаря student из списка students,
# key-функция вернет значение student['score'].
# Именно по этим числам (58, 75, 81, 92) и будет идти сортировка.
sorted_by_score = sorted(students, key=lambda student: student['score'])

# Выведем результат красиво
for student in sorted_by_score:
    print(student)