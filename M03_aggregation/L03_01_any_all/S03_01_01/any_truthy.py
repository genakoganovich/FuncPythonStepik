print(any([False, False, False]))  # -> False (нет ни одного True)
print(any([False, True, False]))   # -> True (есть хотя бы один True)

# А теперь с разными типами данных:
print(any([0, 0, 0]))             # -> False (все элементы "ложные")
print(any([0, 10, 0]))            # -> True (10 - это "истинный" элемент)
print(any(["", None, []]))        # -> False (все элементы "ложные")
print(any(["", "hello", []]))     # -> True ("hello" - "истинный" элемент)