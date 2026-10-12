# import os
# with open("text.txt","w") as f:
#     f.write("hello")
# with open("text.txt","r") as f:
#     print(f.read())  


# try:
#     x=10/0
#     a=9+"9"
#     b=10/2
# except  ZeroDivisionError:
#     print("error")
# else:
#     print("success")
# finally:
#     print("clean-up")

class InvalidAgeError(Exception):
    pass
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18+")
    else:
        print("ok")
check_age(17)
