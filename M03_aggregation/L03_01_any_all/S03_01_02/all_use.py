usernames = ['admin', 'guest', 'user123', 'ann']

# Генераторное выражение, которое проверяет длину каждого имени
# Читается как: "Верни True, если len(name) > 3, для каждого name в usernames"
name_checks = (len(name) > 3 for name in usernames)

# Передаем "ленивый" генератор в all()
is_valid = all(name_checks)

print(f"Все имена пользователей валидны? {is_valid}")
# Вывод: Все имена пользователей валидны? False