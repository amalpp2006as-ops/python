class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class parent(Person):
    def show(self):
        print("Welcome", self.name)


class child(parent):
    def show(self):
        print("Hello", self.name)


a = Person("amal")
b = parent("amal")
c = child("amal")

a.display()
b.show()
c.show()