
a=[1,2,3,4,5]
b = list(map(lambda x: str(x),a))
print(b)


# diff = lambda a, b: abs(a - b)
# print(diff(10, 5))


# area = lambda b, h: 0.5 * b * h
# print(area(10, 5))


# 1. Generate squares of numbers 1 to 100

# result = [x**2 for x in range(1, 101)]
# print(result)


# 2. Extract uppercase letters from a string

# s = "Hello WORLD Python"
# result = [x for x in s if x.isupper()]
# print(result)


# 3. Flatten a nested list

# a = [[1, 2], [3, 4]]
# result = [x for row in a for x in row]
# print(result)


# 4. Replace every even number with its square
    
# numbers = [1, 2, 3, 4, 5, 6]
# result = [x**2 if x % 2 == 0 else x for x in numbers]
# print(result)


# 5. Generate cubes of numbers divisible by 3

# result = [x**3 for x in range(1, 31) if x % 3 == 0]
# print(result)


# 6. Extract words starting with a vowel
    
# s = "apple banana orange elephant umbrella"
# result = [x for x in s.split() if x[0].lower() in "aeiou"]
# print(result)


# 7. Create a list of reversed strings

# words = ["apple", "hello", "python"]
# result = [x[::-1] for x in words]
# print(result)


# 8. Replace all None values with 0

# a = [10, None, 20, None, 30]
# result = [0 if x is None else x for x in a]
# print(result)


# 9. Extract only integers from a mixed list

# a = [10, "hello", 20, 3.5, True, 30]
# result = [x for x in a if type(x) == int]
# print(result)


# 10. Generate Cartesian product of two lists

# a = [1, 2]
# b = [3, 4]
# result = [(x, y) for x in a for y in b]
# print(result)


# 11. Extract the diagonal from a matrix

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = [matrix[i][i] for i in range(len(matrix))]
# print(result)


# 12. Generate all two-digit combinations from digits 1–5

# result = [10*x + y for x in range(1, 6) for y in range(1, 6)]
# print(result)


# 13. Create dictionaries from ID and name lists

# ids = [1, 2, 3]
# names = ["Amal", "John", "David"]
# result = [{"id": i, "name": n} for i, n in zip(ids, names)]
# print(result)


# 14. Convert temperatures to Hot or Cold

# temperatures = [15, 25, 35, 10, 40]
# result = ["Hot" if x >= 30 else "Cold" for x in temperatures]
# print(result)


# 15. Convert numbers to strings but keep integers only

# a = [10, "hello", 20, 3.5, 30]
# result = [str(x) for x in a if type(x) == int]
# print(result)