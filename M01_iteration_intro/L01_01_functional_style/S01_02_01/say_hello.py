def say_hello(name):
  return f"Привет, {name}!"

# Присваиваем саму функцию (без вызова!) переменной
greeting_func = say_hello

# Теперь мы можем вызывать функцию через новую переменную
print(greeting_func("Анна")) # Выведет: Привет, Анна!