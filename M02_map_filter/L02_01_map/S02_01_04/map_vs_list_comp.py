numbers = [1, 2, 3, 4, 5]

# Решение с помощью map() и lambda
squares_map = list(map(
    lambda x: x * x,
    numbers
))

# Решение с помощью спискового включения
squares_lc = [x * x for x in numbers]

print(f"Результат map:    {squares_map}")
print(f"Результат list comp: {squares_lc}")
