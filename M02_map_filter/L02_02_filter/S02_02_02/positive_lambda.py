numbers = [-5, 0, 10, -2, 8, -1, 4]

# Вместо того чтобы определять функцию is_positive,
# мы создаем ее "на лету" прямо внутри filter.

# Читается так: "Оставить только те x, для которых x > 0"
positive_numbers = list(filter(lambda x: x > 0, numbers))

print(positive_numbers)
# Вывод: [10, 8, 4]