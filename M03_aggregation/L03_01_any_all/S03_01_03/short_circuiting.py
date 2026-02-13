import itertools

def infinite_counter():
  """Бесконечный генератор, который считает 1, 2, 3, ..."""
  num = 0
  while True:
    num += 1
    print(f"Генератор выдал: {num}")
    yield num

# Задача: есть ли в бесконечной последовательности чисел
# хотя бы одно, которое делится на 7 без остатка?

result = any(n % 7 == 0 for n in infinite_counter())

print(f"\nРезультат: {result}")