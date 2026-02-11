words = ['stepik', 'python', 'course']

# Сразу "материализуем" результат в список
upper_words_list = list(map(str.upper, words))

# Теперь мы можем использовать этот список сколько угодно раз
print(f"Длина списка: {len(upper_words_list)}")
print("Элементы списка:")
for word in upper_words_list:
  print(f"- {word}")