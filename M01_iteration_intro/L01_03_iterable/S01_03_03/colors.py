# Наш итерируемый объект (iterable)
colors = ['красный', 'зеленый', 'синий']

print(f"Исходный объект: {colors}, тип: {type(colors)}")

# --- Создаем итератор ---
# Python "за кулисами" вызывает colors.__iter__()
colors_iterator = iter(colors)

print(f"Полученный итератор: {colors_iterator}, тип: {type(colors_iterator)}")

# Теперь у нас есть итератор, и мы можем получать из него элементы
# с помощью функции next()
print("\nНачинаем получать элементы:")
print(next(colors_iterator))
print(next(colors_iterator))
print(next(colors_iterator))

# Если мы попробуем вызвать next() еще раз, возникнет ошибка StopIteration,
# так как итератор "исчерпан".