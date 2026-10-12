# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length * self.breadth
# r=Rectangle(5,4)
# print(r.area())

class OddEven:
    def __init__(self,value):
        self.value=value
class OddEven:
    def __init__(self, value):
        self.value = value

    def result(self):
        if self.value % 2 == 0:
            print("is even")
        else:
            print("is odd")


obj = OddEven(10)
obj.result()