# class parent:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"{self.name}")
# class child(parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age=age
#     def display(self):
#         super().display()
#         print(f"{self.name}----{self.age}")
# obj=child("amal",23)
# obj.display()



# class Parent:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"{self.name}")
# class Child(Parent):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#     def display(self):
#         super().display()
#         print(f"{self.name}---{self.age}")
# obj=Child("sneha",45)
# obj.display()



# mulilevel inheritence

# class A:
#     def hello(self):
#         print("hello")
# class B(A):
#     def hai(self):
#         print("hai")
# class C(B):
#     def hoi(self):
#         pass
# obj=B()
# obj.hello()
# obj.hai()


# Muliple inheritence

# class A:
#     def greet(self):
#         print("Hello from A")
# class B:
#     def greet(self):
#         print("Hello from B")
# class C(A, B):
#     pass

# obj = C()
# obj.greet()  
# print(C.mro())


# class Bank:
#     def __init__(self,name,dept,salary):
#         self.name=name
#         self._dept=dept
#         self.__salary=salary
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self,amount):
#         if amount > 0 :
#             self.__salary=amount
# b=Bank("amal","Manager",5000000)
# print(b.name)
# print(b._dept)
# print(b.get_salary)
# print(b.get_salary())
# b.set_salary(55000)
# print(b.get_salary())
