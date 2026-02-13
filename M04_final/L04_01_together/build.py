data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Строим конвейер в одну строку
# Читать его нужно "изнутри наружу"
final_result = sum(
    map(lambda x: x * x,
        filter(lambda x: x % 2 == 0, data)
    )
)

print(f"Результат, полученный конвейером: {final_result}") # -> 220