# square = [x **2 for x in range (1,101)]
# print(square)

# text = "Hello Amal Pp PYThOn MY world"
# uppercase =[x for x in text if x.isupper()]
# print(uppercase)

# a =[[1,2],[3,4]] 
# b=[x for sublist in a for x in sublist]
# print(a)
# print(b)


# b = [x for x in range(1,8) if x ]

# 1. Generate squares of numbers 1 to 100 using list comprehension.
# Answer:

# squares = [x**2 for x in range(1, 101)]
# print(squares)


# 2. Extract all uppercase letters from a string.
# Answer:

# text = "Hello WORLD Python"
# result = [x for x in text if x.isupper()]
# print(result)


# 3. Convert nested list [[1,2],[3,4]] into [1,2,3,4].
# Answer:

# lst = [[1, 2], [3, 4]]
# result = [x for sublist in lst for x in sublist]
# print(result)


# 4. Create a new list replacing every even number with its square.
# Answer:

# numbers = [1, 2, 3, 4, 5, 6]
# result = [x**2 if x % 2 == 0 else x for x in numbers]
# print(result)


# 5. Generate a list of cubes for numbers divisible by 3.
# Answer:

# numbers = range(1, 21)
# result = [x**3 for x in numbers if x % 3 == 0]
# print(result)


# 6. Extract words starting with a vowel from a sentence.
# Answer:

# sentence = "An apple is on the orange table"
# result = [x for x in sentence.split() if x[0].lower() in "aeiou"]
# print(result)


# 7. Create a list of reversed strings.
# Answer:

# words = ["hello", "python", "world"]
# result = [x[::-1] for x in words]
# print(result)


# 8. Replace all None values in a list with 0.
# Answer:

# numbers = [1, None, 3, None, 5]
# result = [0 if x is None else x for x in numbers]
# print(result)


# 9. Extract only integers from a mixed list.
# Answer:

# lst = [1, "hello", 2.5, 3, "python", 4]
# result = [x for x in lst if isinstance(x, int) and not isinstance(x, bool)]
# print(result)


# 10. Generate Cartesian product for two lists.
# Answer:

# list1 = [1, 2, 3]
# list2 = ["A", "B"]
# result = [(x, y) for x in list1 for y in list2]
# print(result)


# 11. From a matrix, extract the diagonal into a new list.
# Answer:

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = [matrix[i][i] for i in range(len(matrix))]
# print(result)


# 12. Generate all two-digit combinations from digits 1–5.
# Answer:

# result = [10*x + y for x in range(1, 6) for y in range(1, 6)]
# print(result)


# 13. Create a list of dictionaries from two lists (id and name).
# Answer:

# ids = [1, 2, 3]
# names = ["Amal", "Rahul", "Arun"]
# result = [{"id": i, "name": n} for i, n in zip(ids, names)]
# print(result)


# 14. Convert a list of temperatures to 'Hot' or 'Cold'.
# Answer:

# temperatures = [15, 25, 35, 10, 40]
# result = ["Hot" if x >= 30 else "Cold" for x in temperatures]
# print(result)


# 15. Convert a list of numbers into strings but keep integers only.
# Answer:

# numbers = [1, 2.5, 3, 4.7, 5, "hello"]
# result = [str(x) for x in numbers if isinstance(x, int) and not isinstance(x, bool)]
# print(result)