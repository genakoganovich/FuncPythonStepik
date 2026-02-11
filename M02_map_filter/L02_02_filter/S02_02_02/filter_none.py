data = ["яблоко", "", "банан", None, "вишня", 0, []]

# filter(None, ...) — это специальный короткий синтаксис.
# Он автоматически отфильтровывает все элементы, которые являются False-подобными.
# Это эквивалентно filter(lambda x: bool(x), data)
non_empty_data = list(filter(None, data))

print(non_empty_data)
# Вывод: ['яблоко', 'банан', 'вишня']