def get_multiplier(factor):
  # Эта функция создает и возвращает другую функцию
  def multiplier(number):
    return number * factor
  return multiplier

# Создаем функцию, которая будет умножать на 2
multiply_by_2 = get_multiplier(2)
# Создаем функцию, которая будет умножать на 5
multiply_by_5 = get_multiplier(5)

print(multiply_by_2(10)) # Выведет: 20
print(multiply_by_5(10)) # Выведет: 50