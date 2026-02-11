def add_one(n):
  return n + 1

def apply_operation(operation_func, value):
  # Мы вызываем функцию, которую нам передали
  result = operation_func(value)
  print(f"Результат: {result}")

# Передаем функцию add_one как аргумент
apply_operation(add_one, 10) # Выведет: Результат: 11