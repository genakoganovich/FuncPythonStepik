words = ['яблоко', 'банан', 'вишня']
# x — это каждое отдельное слово
lengths = list(map(
    lambda x: len(x),
    words
))
print(lengths)
# Вывод: [6, 5, 5]