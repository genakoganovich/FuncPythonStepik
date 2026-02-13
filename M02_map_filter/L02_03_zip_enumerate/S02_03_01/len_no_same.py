letters = ['a', 'b', 'c', 'd'] # 4 элемента
numbers = [1, 2, 3]          # 3 элемента

result = list(zip(letters, numbers))

print(result)
# Вывод: [('a', 1), ('b', 2), ('c', 3)]
# Элемент 'd' был проигнорирован, так как для него нет пары в numbers.