# number = [23,45,56,43,53,54]

# a = {x:x**3 for x in number if x%2 != 0}

# print(a)

# numbers = [-3, -1, 0, 2, 5]
# a = { x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero" for x in numbers}
# print(a)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for k, v in list(d.items()):
#     if v % 2 != 0:
#         d.pop(k)
# print(d)

# # 1. Create a dictionary mapping numbers 1–20 to their cubes.

# result = {x: x**3 for x in range(1, 21)}
# print(result)


# # 2. From a string, build a dictionary of vowels and their counts.

# text = "hello world"
# result = {x: text.count(x) for x in "aeiou" if x in text}
# print(result)


# # 3. Create a dictionary mapping a word to its reversed form.

# words = ["hello", "python", "world"]
# result = {x: x[::-1] for x in words}
# print(result)


# # 4. Convert a list of tuples to dict but skip tuples with None.

# data = [("a", 1), ("b", None), ("c", 3)]
# result = {k: v for k, v in data if v is not None}
# print(result)


# # 5. Build a dictionary of items and prices with discount applied.

# prices = {"apple": 100, "banana": 50, "orange": 80}
# result = {k: v * 0.9 for k, v in prices.items()}
# print(result)


# # 6. Filter dictionary to keep keys that start with a vowel.

# data = {"apple": 1, "banana": 2, "orange": 3, "grape": 4}
# result = {k: v for k, v in data.items() if k[0].lower() in "aeiou"}
# print(result)


# # 7. Build a dictionary of index: value for a given list.

# items = ["apple", "banana", "orange"]
# result = {i: v for i, v in enumerate(items)}
# print(result)


# # 8. Create a dict mapping numbers to 'positive', 'negative', or 'zero'.

# numbers = [-2, -1, 0, 1, 2]
# result = {x: "positive" if x > 0 else "negative" if x < 0 else "zero" for x in numbers}
# print(result)


# # 9. Build a frequency dictionary of words in a sentence.

# sentence = "python is easy and python is powerful"
# words = sentence.split()
# result = {x: words.count(x) for x in words}
# print(result)


# # 10. Reverse a dictionary but only keep unique values.

# data = {"a": 1, "b": 2, "c": 1, "d": 3}
# result = {v: k for k, v in data.items() if list(data.values()).count(v) == 1}
# print(result)


# # 11. Create a dictionary of prime numbers and True/False.

# numbers = range(1, 21)
# result = {
#     x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
#     for x in numbers
# }
# print(result)


# # 12. Convert a list into a dictionary with counts using comprehension.

# items = ["apple", "banana", "apple", "orange", "banana", "apple"]
# result = {x: items.count(x) for x in items}
# print(result)


# # 13. Build a dict of numbers 1–30 and mark them 'odd' or 'even'.

# result = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 31)}
# print(result)


# # 14. Build a dict from two lists but only if their lengths match.

# keys = ["a", "b", "c"]
# values = [10, 20, 30]

# result = {keys[i]: values[i] for i in range(len(keys))} if len(keys) == len(values) else {}
# print(result)


# # 15. Create a dictionary mapping student names to pass/fail by marks.

# marks = {"Amal": 85, "Rahul": 35, "Arun": 60, "Anu": 25}
# result = {name: "Pass" if mark >= 40 else "Fail" for name, mark in marks.items()}
# print(result)