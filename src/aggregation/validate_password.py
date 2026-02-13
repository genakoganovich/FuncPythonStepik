s = input()
print(all([len(s) >= 8, any(x.isdigit() for x in s), any(x.isupper() for x in s)]))
