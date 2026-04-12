# def sq(number):
#     return number**2
#
# print(sq(2))

# sum of 2 num
# def sum(a,b) :
#     return a+b
# print(sum(2,5))

# fn multipy that 2 num but can also accept and multipy string
# def multi(a,b):
#     return a*b
# print(multi(8,5))
# print(multi('a',5))
# print(multi(5,'a'))

# area and circumference of circle
# import math
# def circle(r):
#     a=math.pi* r**2
#     c=2*math.pi*r
#     return a,c
#
# a,c=circle(4)
# print("area: ",a," circumference: ",c)

# greet user
# def greet(name="user"):
#     return "hello, "+name+" !"

# lamda fn to compute the cube of a num
# cube =lambda x:x**3
# # print(cube(3))

# fn that takes variable num of argument and return their sum
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1,2,3,4))
# print(sum_all(1,23))

# **kwargs
# def print_kwargs(name,power):
#     print("Name ",name," P ower ",power)
#
# print_kwargs(name ="shaktiman", power="lazer")

# def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# print_kwargs(name="shaktiman",power="lazer")
# print_kwargs(name="shaktiman")
# print_kwargs(name="shaktiman",power ="lazer", enemy="dr. meeshi")

# generator fn that yields even no. up to specific limit
# def even_generator(limit):
#     li=[]
#     for i in range(2,limit+1,2):
#          li.append(i)
#     return li
# print(even_generator(10))

# def even_generator(limit):
#     for i in range(2,limit+1, 2):
#         yield i
# for num in even_generator(10):
#     print(num)

# recursive fn of factorial
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(4))