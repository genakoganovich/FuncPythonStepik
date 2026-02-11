numbers = [10, 20, 30, 40]

# Вместо имени внешней функции мы пишем код функции прямо внутри
result = list(map(
    lambda x: x + 5,
    numbers
))

print(result)
# Вывод: [15, 25, 35, 45]