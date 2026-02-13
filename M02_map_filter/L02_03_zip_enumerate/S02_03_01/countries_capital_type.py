countries = ['Россия', 'США', 'Франция']
capitals = ['Москва', 'Вашингтон', 'Париж']

zipped_object = zip(countries, capitals)
print(zipped_object)
# Вывод: <zip object at 0x...>

# Чтобы увидеть все содержимое, нужно "материализовать" итератор
list_of_tuples = list(zipped_object)
print(list_of_tuples)
# Вывод: [('Россия', 'Москва'), ('США', 'Вашингтон'), ('Франция', 'Париж')]