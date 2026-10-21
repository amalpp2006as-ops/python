# dif = lambda a,b:a-b
# print(dif(54,5))


# numbers = [1,2,3,4,5]

# result = list(map(lambda x: str(x), numbers))

# print(result)


# base=int(input("enter Base : "))
# height=int(input("enter height : "))

# area  = lambda  base,height:0.5*base*height
# print("Area : ",area(base,height))

# a =list(map(int,input("enter numbers : ").split()))
# print(a)

# result = list(filter(lambda x: x % 10 == 5, a))
# print(result)

# for i in range(1,10):
#     if i==2: 
#         continue
#     elif i==6:
#         break
#     print(i)

# a=3*"3"
# print(a)

# a=[[1,2],[3,4],[5,6]]
# b=[]
# for i in a:
#     for j in i:
#         b.append(j)

# print(b)  


a=[1,2,3,4,5,6]
n=3
b=[]
for i in a:
    for i in range(0, len(a), n):
        a.append(a[1:i+n])
print(b)           

