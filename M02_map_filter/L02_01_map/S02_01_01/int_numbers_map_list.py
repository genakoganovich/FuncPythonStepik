str_numbers = ['1', '5', '10', '25']

# 1. Создаем ленивый итератор map
int_numbers_map = map(int, str_numbers)

# 2. Преобразуем итератор в список, чтобы увидеть результат
# Именно на этом шаге происходят все вычисления!
final_list = list(int_numbers_map)

print(final_list)
# Вывод: [1, 5, 10, 25]