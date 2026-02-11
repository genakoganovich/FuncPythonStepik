str_numbers = ['1', '5', '10', '25']

# Мы говорим: "Примени функцию int к каждому элементу списка str_numbers"
int_numbers_map = map(int, str_numbers)

print(int_numbers_map)
# Вывод: <map object at 0x...>