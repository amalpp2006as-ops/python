class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Parent(Person):
    def show(self):
        print("Welcome", self.name)


class child(Parent):
    def show(self):
        print("Hello", self.name)


a = Person("amal")
b = Parent("rahul")
c = child("lol")

a.show()
b.show()
c.show()

