tasks = ['Помыть посуду', 'Выучить Python', 'Сделать зарядку']
enum_object = enumerate(tasks)
print(enum_object)
# Вывод: <enumerate object at 0x...>

# Чтобы увидеть содержимое, нужно его "материализовать"
list_of_tuples = list(enum_object)
print(list_of_tuples)
# Вывод: [(0, 'Помыть посуду'), (1, 'Выучить Python'), (2, 'Сделать зарядку')]