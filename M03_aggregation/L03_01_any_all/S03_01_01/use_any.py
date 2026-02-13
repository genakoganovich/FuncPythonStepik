measurements = [10.5, 12.1, 13.4, -2.5, 11.9, 8.0]

# Создаем генератор, который будет выдавать True для отрицательных чисел
# и False для положительных.
# Читается как: "Верни True, если value < 0, для каждого value в measurements"
error_checks = (value < 0 for value in measurements)

# Теперь передаем этот "ленивый" генератор в any()
result = any(error_checks)

print(f"Была ли ошибка? {result}")
# Вывод: Была ли ошибка? True