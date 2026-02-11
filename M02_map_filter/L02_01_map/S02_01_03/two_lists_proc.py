prices = [100, 200, 300]
discounts = [0.1, 0.2, 0.15] # Скидки: 10%, 20%, 15%

# price берется из первого списка, discount из второго
final_prices = list(map(
    lambda price, discount: price * (1 - discount),
    prices,
    discounts
))

print(final_prices)
# Вывод: [90.0, 160.0, 255.0]