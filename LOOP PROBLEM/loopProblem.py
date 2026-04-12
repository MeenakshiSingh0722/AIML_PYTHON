# count positive number
# num=[1,-2,-4,7,6,5,3,8,-9]
# pos_num_count=0
# for num in num:
#     if num>0:
#         pos_num_count+=1
# print("final count is :",pos_num_count)

# sum of even number
# n=int(input("enter your num: "))
# sum_even=0
# for i in range(1,n+1):
#     if (i%2==0):
#         sum_even+=i
# print("sum of even num is: ",sum_even)

# multiplication table
# n=int(input("enter a num: "))
# for i in range(1,11):
#     if n==5:
#         continue
#     print(n, ' X',i,' =',n*i)

# reverse a string
# n=input("enter your string: ")
# rev=""
# for char in n:
#     rev=char+rev
# print(rev)

# find the first non-repeated char
# n=input("enter a num")
# for char in n:
#     if n.count(char)==1:
#         print("char is: ",char)
#         break

# factorial
# n=int(input("enter a num: "))
# fact=1
# while n>0:
#     fact=fact*n
#     n-=1
# print("fact is: ",fact)

# # keep asking the user for ip until they enter a num between 1 and 100
# while True:
#     n=int(input("Enter a num between 1 and 100"))
#     if 1<= n <=10:
#         print("thanxx")
#         break
#     else:
#         print("invalid num try again")

#check prime num
# n=int(input("enter a number: "))
# is_prime=True
# if n>1:
#     for i in range(2,n):
#         if(n%i)==0:
#             is_prime=False
#             break
#
# print(is_prime)

# list uniqueness checker
# i=["apple","banana","orange","apple","mango"]
# unique=set()
# for item in i:
#     if item in unique:
#         print("Duplicate ",item)
#         break
#     unique.add(item)

# exponential backoff :that doubles the wait time between retries, starting from 1sec , but stops after 5sec
# import time
# wait_time=1
# max_retries=5
# attempts=0
#
# while attempts< max_retries:
#     print("attempt ",attempts+1 , "- wait time", wait_time)
#     time.sleep(wait_time)
#     wait_time*=2
#     attempts+=1