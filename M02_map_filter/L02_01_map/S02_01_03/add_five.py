def add_five(number):
    """Эта функция просто прибавляет 5 к числу."""
    return number + 5

numbers = [10, 20, 30, 40]

# Передаем имя функции в map
result = list(map(add_five, numbers))

print(result)
# Вывод: [15, 25, 35, 45]