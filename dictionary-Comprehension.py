number = [23,45,56,43,53,54]

a = {x:x**3 for x in number if x%2 != 0}

print(a)