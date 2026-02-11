numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Условие: остаток от деления на 2 равен 0
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

print(even_numbers)
# Вывод: [2, 4, 6, 8, 10]