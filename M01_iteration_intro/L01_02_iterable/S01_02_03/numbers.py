numbers = [10, 20, 30]

# Создаем итератор
num_iterator = iter(numbers)

# Пройдемся по нему в цикле for (цикл автоматически вызывает next() до конца)
print("Первый проход по итератору:")
for num in num_iterator:
    print(num)

# Итератор исчерпан. Попытаемся пройтись по нему еще раз.
print("\nВторой проход по тому же итератору:")
for num in num_iterator:
    print(num) # Этот код ничего не выведет!

# Если бы мы попытались вызвать next() вручную, получили бы ошибку:
# next(num_iterator) -> StopIteration
# ... (продолжение предыдущего кода)

# Чтобы пройтись снова, создаем НОВЫЙ итератор
new_num_iterator = iter(numbers)

print("\nПроход по новому итератору:")
print(next(new_num_iterator)) # Выведет 10