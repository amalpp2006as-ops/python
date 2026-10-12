# def sum_num(a,b):
#   result=a+b
#   return result
# print(sum_num(a=5,b=6))

# x=3
# y=4
# z=5
# a = lambda x,y,z:0.5*x*y*z
# print(a(x,y,z)) 

# x=[1,2,3,4,5,6]
# y= lambda x:x[3]
# print(y(x))


# x = lambda a,b:a-b
# print(x(a=50,b=23))

# a = [1,2,3,4,5,6]
# x =list(map(lambda x:x**3,a))
# print(x)

# a = [1,2,3,4,5,6]
# x =list(filter(lambda x:x%2==0,a))
# print(x)

def pattern(n):
    for i in range(1, n + 1):
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()

pattern(5)


