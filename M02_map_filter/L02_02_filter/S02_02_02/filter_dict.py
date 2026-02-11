students = [
    {'name': 'Анна', 'score': 92},
    {'name': 'Борис', 'score': 58},
    {'name': 'Виктор', 'score': 75},
    {'name': 'Галина', 'score': 45},
    {'name': 'Дмитрий', 'score': 81}
]

# Условие: значение по ключу 'score' в словаре student должно быть больше 60
passed_students = list(filter(lambda student: student['score'] > 60, students))

print(passed_students)
# Вывод:
# [{'name': 'Анна', 'score': 92}, {'name': 'Виктор', 'score': 75}, {'name': 'Дмитрий', 'score': 81}]