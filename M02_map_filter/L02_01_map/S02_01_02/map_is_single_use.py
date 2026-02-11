words = ['stepik', 'python', 'course']
upper_words_iterator = map(str.upper, words)

# Первый раз проходим по итератору. Все работает отлично.
print("Первый проход:")
word_list_1 = list(upper_words_iterator)
print(word_list_1) # Вывод: ['STEPIK', 'PYTHON', 'COURSE']

# Пытаемся пройти по ТОМУ ЖЕ итератору еще раз.
print("\nВторой проход:")
word_list_2 = list(upper_words_iterator)
print(word_list_2) # Вывод: []