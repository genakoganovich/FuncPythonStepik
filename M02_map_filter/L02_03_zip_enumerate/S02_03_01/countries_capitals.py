countries = ['Россия', 'США', 'Франция']
capitals = ['Москва', 'Вашингтон', 'Париж']

# zip "сцепляет" списки
# Мы сразу распаковываем кортежи в переменные country и capital
for country, capital in zip(countries, capitals):
  print(f"{country} - {capital}")