# # 5. Create a class Rectangle with methods to calculate area and perimeter.

# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth

#     def perimeter(self):
#         return 2 * (self.length + self.breadth)

# r = Rectangle(10, 5)
# print("Area:", r.area())
# print("Perimeter:", r.perimeter())


# # 6. Implement multiple inheritance for Printer, Scanner, and AllInOneMachine.

# class Printer:
#     def print_document(self):
#         print("Printing document")

# class Scanner:
#     def scan_document(self):
#         print("Scanning document")

# class AllInOneMachine(Printer, Scanner):
#     pass

# obj = AllInOneMachine()
# obj.print_document()
# obj.scan_document()


# # 7. Build Employee class with salary calculation including bonuses and deductions.

# class Employee:
#     def __init__(self, name, salary, bonus, deduction):
#         self.name = name
#         self.salary = salary
#         self.bonus = bonus
#         self.deduction = deduction

#     def calculate_salary(self):
#         return self.salary + self.bonus - self.deduction

# e = Employee("Amal", 25000, 5000, 2000)
# print("Employee:", e.name)
# print("Final Salary:", e.calculate_salary())


# # 8. Create a class Vector that overloads the + operator to add two vectors.

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def display(self):
#         print(self.x, self.y)

# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# v3 = v1 + v2
# v3.display()


# # 9. Build a Library system: Book and Library classes. Add borrow/return features.

# class Book:
#     def __init__(self, title):
#         self.title = title
#         self.available = True

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def borrow_book(self, title):
#         for book in self.books:
#             if book.title == title and book.available:
#                 book.available = False
#                 print("Book borrowed")
#                 return
#         print("Book not available")

#     def return_book(self, title):
#         for book in self.books:
#             if book.title == title and not book.available:
#                 book.available = True
#                 print("Book returned")
#                 return
#         print("Book not found or already returned")

# library = Library()
# library.add_book(Book("Python"))
# library.borrow_book("Python")
# library.return_book("Python")


# # 10. Create a class Temperature that converts Celsius to Fahrenheit and vice versa.

# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius

#     def to_fahrenheit(self):
#         return (self.celsius * 9/5) + 32

#     @staticmethod
#     def to_celsius(fahrenheit):
#         return (fahrenheit - 32) * 5/9

# t = Temperature(25)
# print("Fahrenheit:", t.to_fahrenheit())
# print("Celsius:", Temperature.to_celsius(98.6))


# # 11. Implement an abstract class Shape with subclasses Circle and Square.

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# c = Circle(5)
# s = Square(4)
# print("Circle Area:", c.area())
# print("Square Area:", s.area())


# # 12. Create a class Queue using OOP (enqueue, dequeue).

# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if self.items:
#             return self.items.pop(0)
#         return "Queue is empty"

# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# print(q.dequeue())
# print(q.items)


# # 13. Make a Product class with discount calculation.

# class Product:
#     def __init__(self, name, price, discount):
#         self.name = name
#         self.price = price
#         self.discount = discount

#     def final_price(self):
#         return self.price - (self.price * self.discount / 100)

# p = Product("Laptop", 50000, 10)
# print("Final Price:", p.final_price())


# # 14. Implement polymorphism using method overriding between classes Vehicle and Bike.

# class Vehicle:
#     def start(self):
#         print("Vehicle starts")

# class Bike(Vehicle):
#     def start(self):
#         print("Bike starts")

# v = Vehicle()
# b = Bike()
# v.start()
# b.start()


# # 15. Build a class Calculator that supports addition using __add__ operator overloading.

# class Calculator:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return Calculator(self.value + other.value)

# c1 = Calculator(10)
# c2 = Calculator(20)
# c3 = c1 + c2
# print("Sum:", c3.value)


# # 16. Create custom exception class InvalidAgeError and use it for age validation.

# class InvalidAgeError(Exception):
#     pass

# age = int(input("Enter age: "))

# try:
#     if age < 18:
#         raise InvalidAgeError("Age must be 18 or above")
#     print("Valid age")
# except InvalidAgeError as e:
#     print(e)


# # 17. Create a class School that stores a list of Students and displays toppers.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# class School:
#     def __init__(self):
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def display_topper(self):
#         if self.students:
#             topper = max(self.students, key=lambda s: s.marks)
#             print("Topper:", topper.name)
#             print("Marks:", topper.marks)

# school = School()
# school.add_student(Student("Amal", 85))
# school.add_student(Student("Rahul", 90))
# school.add_student(Student("Arun", 75))
# school.display_topper()


# # 18. Build a class Timer that uses __enter__ and __exit__ to measure execution time.

# import time

# class Timer:
#     def __enter__(self):
#         self.start = time.time()
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.end = time.time()
#         print("Execution Time:", self.end - self.start)

# with Timer():
#     time.sleep(2)


# # 19. Create a class ConfigLoader that reads JSON config and provides getter methods.

# import json

# class ConfigLoader:
#     def __init__(self, filename):
#         with open(filename, "r") as file:
#             self.config = json.load(file)

#     def get(self, key):
#         return self.config.get(key)

# # config.json should contain: {"name": "Amal", "age": 20}
# config = ConfigLoader("config.json")
# print(config.get("name"))
# print(config.get("age"))


# # 20. Build a class Playlist that manages songs using list operations.

# class Playlist:
#     def __init__(self):
#         self.songs = []

#     def add_song(self, song):
#         self.songs.append(song)

#     def remove_song(self, song):
#         if song in self.songs:
#             self.songs.remove(song)

#     def display(self):
#         print(self.songs)

# p = Playlist()
# p.add_song("Song 1")
# p.add_song("Song 2")
# p.display()
# p.remove_song("Song 1")
# p.display()


# # 21. Implement a singleton class using __new__.

# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

# a = Singleton()
# b = Singleton()
# print(a is b)


# # 22. Create a class Polygon with dynamic number of sides using *args.

# class Polygon:
#     def __init__(self, *sides):
#         self.sides = sides

#     def display(self):
#         print("Sides:", self.sides)
#         print("Number of sides:", len(self.sides))

# p = Polygon(3, 4, 5)
# p.display()


# # 23. Build a UserAuthentication system using OOP.

# class UserAuthentication:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def login(self, username, password):
#         if self.username == username and self.password == password:
#             print("Login successful")
#         else:
#             print("Invalid username or password")

# user = UserAuthentication("amal", "1234")
# user.login("amal", "1234")


# # 24. Create a class ChatMessage with timestamp formatting.

# from datetime import datetime

# class ChatMessage:
#     def __init__(self, sender, message):
#         self.sender = sender
#         self.message = message
#         self.timestamp = datetime.now()

#     def display(self):
#         print("Sender:", self.sender)
#         print("Message:", self.message)
#         print("Time:", self.timestamp.strftime("%d-%m-%Y %H:%M:%S"))

# chat = ChatMessage("Amal", "Hello")
# chat.display()


# # 25. Implement custom iterable class NumberSeries using __iter__.

# class NumberSeries:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return iter(range(self.start, self.end + 1))

# numbers = NumberSeries(1, 5)

# for x in numbers:
#     print(x)


# # 26. Build a class History that tracks operations using a list.

# class History:
#     def __init__(self):
#         self.operations = []

#     def add_operation(self, operation):
#         self.operations.append(operation)

#     def display(self):
#         print(self.operations)

# h = History()
# h.add_operation("Addition")
# h.add_operation("Subtraction")
# h.display()


# # 27. Create a class Mailbox with add_mail, delete_mail methods.

# class Mailbox:
#     def __init__(self):
#         self.mails = []

#     def add_mail(self, mail):
#         self.mails.append(mail)

#     def delete_mail(self, mail):
#         if mail in self.mails:
#             self.mails.remove(mail)

#     def display(self):
#         print(self.mails)

# m = Mailbox()
# m.add_mail("Email 1")
# m.add_mail("Email 2")
# m.display()
# m.delete_mail("Email 1")
# m.display()


# # 28. Implement deep copy behavior in a class using copy module.

# import copy

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("Amal", [80, 90, 85])
# s2 = copy.deepcopy(s1)

# s2.marks[0] = 50

# print("Original:", s1.marks)
# print("Copied:", s2.marks)


# # 29. Build a class Order that calculates tax, GST, and total bill.

# class Order:
#     def __init__(self, price, gst_rate):
#         self.price = price
#         self.gst_rate = gst_rate

#     def calculate_gst(self):
#         return self.price * self.gst_rate / 100

#     def total_bill(self):
#         return self.price + self.calculate_gst()

# order = Order(1000, 18)
# print("GST:", order.calculate_gst())
# print("Total Bill:", order.total_bill())


# # 30. Create a class Graph with methods to add nodes and edges.

# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def add_node(self, node):
#         if node not in self.graph:
#             self.graph[node] = []

#     def add_edge(self, node1, node2):
#         self.add_node(node1)
#         self.add_node(node2)
#         self.graph[node1].append(node2)
#         self.graph[node2].append(node1)

#     def display(self):
#         print(self.graph)

# g = Graph()
# g.add_node("A")
# g.add_edge("A", "B")
# g.add_edge("A", "C")
# g.display()