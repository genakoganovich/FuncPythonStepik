names = ['Анна', 'борис', 'Виктор']

# Метод .lower() приводит строку к нижнему регистру перед сравнением
sorted_case_insensitive = sorted(names, key=lambda name: name.lower())

print(sorted_case_insensitive)
# Вывод: ['Анна', 'борис', 'Виктор'] (порядок 'а', 'б', 'в')