my_list = ['Python', 'Stepik', 'Course']

# 1. Получаем итератор из нашего итерируемого объекта (списка)
my_iterator = iter(my_list)

print(f"Тип объекта my_list: {type(my_list)}")
print(f"Тип объекта my_iterator: {type(my_iterator)}") # Обратите внимание на тип!

# 2. Получаем элементы из итератора один за другим
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# 3. Что будет, если попросить еще один элемент?
# Следующая строка вызовет ошибку StopIteration, потому что элементы закончились.
# Мы ее закомментируем, но вы можете запустить у себя и проверить.
# print(next(my_iterator))