ids = [101, 102, 103]
# Превращаем числа в строки с префиксом
formatted = list(map(
    lambda x: f"ID-{x}",
    ids
))
print(formatted)
# Вывод: ['ID-101', 'ID-102', 'ID-103']