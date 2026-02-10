# Список наших данных
numbers = [1, 2, 3, 4, 5]

# --- Определим несколько простых функций-операций ---
def square(n):
  """Возводит число в квадрат."""
  return n * n

def cube(n):
  """Возводит число в куб."""
  return n * n * n

def is_even(n):
  """Возвращает True, если число четное."""
  return n % 2 == 0

# --- А теперь создадим нашу "универсальную" функцию ---
# Она принимает список и ДРУГУЮ ФУНКЦИЮ в качестве аргументов.
def process_list(data_list, operation_func):
  """
  Применяет функцию operation_func к каждому элементу списка data_list.
  """
  result_list = []
  for item in data_list:
    # Вызываем переданную нам функцию для каждого элемента
    result_list.append(operation_func(item))
  return result_list

# --- Используем нашу универсальную функцию ---

# 1. Применим операцию возведения в квадрат
squared_numbers = process_list(numbers, square)
print(f"Числа в квадрате: {squared_numbers}")

# 2. А теперь применим операцию возведения в куб, ИСПОЛЬЗУЯ ТУ ЖЕ ФУНКЦИЮ!
cubed_numbers = process_list(numbers, cube)
print(f"Числа в кубе: {cubed_numbers}")

# 3. А можно и проверить на четность
even_flags = process_list(numbers, is_even)
print(f"Проверка на четность: {even_flags}")