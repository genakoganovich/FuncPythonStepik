transactions = [
    {'id': 1, 'amount': 100, 'currency': 'USD', 'status': 'completed'},
    {'id': 2, 'amount': 50,  'currency': 'EUR', 'status': 'completed'},
    {'id': 3, 'amount': 200, 'currency': 'USD', 'status': 'failed'},
    {'id': 4, 'amount': 75,  'currency': 'USD', 'status': 'completed'},
    {'id': 5, 'amount': 120, 'currency': 'EUR', 'status': 'completed'},
    {'id': 6, 'amount': 30,  'currency': 'USD', 'status': 'completed'},
    {'id': 7, 'amount': 90,  'currency': 'USD', 'status': 'failed'},
]

# Читаем изнутри наружу:
# 1. filter отбирает нужные транзакции
# 2. map извлекает из них суммы
# 3. sum складывает эти суммы
total_revenue_pipeline = sum(
    map(
        lambda t: t['amount'],
        filter(
            lambda t: t['status'] == 'completed' and t['currency'] == 'USD',
            transactions
        )
    )
)

print(f"Результат, полученный конвейером: {total_revenue_pipeline}") # -> 205