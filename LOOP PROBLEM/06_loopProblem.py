# factorial
n=int(input("enter a num: "))
fact=1
while n>0:
    fact=fact*n
    n-=1
print("fact is: ",fact)