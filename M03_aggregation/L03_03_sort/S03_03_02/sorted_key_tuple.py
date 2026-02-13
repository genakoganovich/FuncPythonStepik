products = [('яблоко', 50), ('банан', 30), ('вишня', 45)]

# Сортируем по цене (элемент с индексом 1)
sorted_by_price = sorted(products, key=lambda item: item[1])

print(sorted_by_price)
# Вывод: [('банан', 30), ('вишня', 45), ('яблоко', 50)]