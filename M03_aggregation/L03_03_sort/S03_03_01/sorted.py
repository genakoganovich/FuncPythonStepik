numbers = [30, 10, 50, 20, 40]
print(f"Исходный список: {numbers}")

# Вызываем функцию sorted()
sorted_numbers = sorted(numbers)

print(f"Что вернула функция sorted(): {sorted_numbers}")
print(f"Исходный список ПОСЛЕ sorted(): {numbers}") # Он не изменился!