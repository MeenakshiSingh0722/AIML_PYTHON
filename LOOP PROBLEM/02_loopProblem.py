# sum of even number
n=int(input("enter your num: "))
sum_even=0
for i in range(1,n+1):
    if (i%2==0):
        sum_even+=i
print("sum of even num is: ",sum_even)