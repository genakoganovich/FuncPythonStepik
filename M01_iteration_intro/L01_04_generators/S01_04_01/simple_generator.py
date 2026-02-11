def simple_generator():
  print("Генератор стартовал...")
  yield 1
  print("Генератор возобновил работу...")
  yield 2
  print("И еще раз...")
  yield 3
  print("Генератор завершает работу.")

# 1. Создаем объект-генератор.
# ВАЖНО: Код внутри функции еще НЕ ВЫПОЛНЯЕТСЯ!
my_gen = simple_generator()

print(f"Создали генератор: {my_gen}")
print("-" * 20)

# 2. Первый вызов next()
# Код функции выполняется до первого yield.
value = next(my_gen)
print(f"Получили значение: {value}")
print("-" * 20)

# 3. Второй вызов next()
# Функция "размораживается" и продолжает работу до второго yield.
value = next(my_gen)
print(f"Получили значение: {value}")
print("-" * 20)

# 4. Третий вызов next()
value = next(my_gen)
print(f"Получили значение: {value}")
print("-" * 20)

# 5. Четвертый вызов next()
# Функция доходит до конца, не встречая больше yield,
# и автоматически вызывает StopIteration.
# next(my_gen) # -> вызовет ошибку StopIteration
next(my_gen)