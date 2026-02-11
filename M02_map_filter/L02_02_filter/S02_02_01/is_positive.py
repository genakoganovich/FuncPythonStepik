def is_positive(number):
  return number > 0

numbers = [-5, 0, 10, -2, 8, -1, 4]

# 1. Создаем ленивый итератор filter
positive_numbers_filter = filter(is_positive, numbers)

# 2. Преобразуем итератор в список, чтобы запустить процесс фильтрации
final_list = list(positive_numbers_filter)

print(final_list)
# Вывод: [10, 8, 4]