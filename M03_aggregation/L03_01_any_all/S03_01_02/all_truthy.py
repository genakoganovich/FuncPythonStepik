print(all([True, True, True]))      # -> True (все элементы True)
print(all([True, False, True]))     # -> False (есть один False)

# С разными типами данных
print(all([1, 10, "hello", [1]]))   # -> True (все элементы "истинные")
print(all([1, 0, "hello"]))         # -> False (0 - это "ложный" элемент)
print(all(["ok", "ok", ""]))        # -> False ("" - пустая строка, "ложный" элемент)