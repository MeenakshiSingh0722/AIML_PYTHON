# find the first non-repeated char
n=input("enter a num")
for char in n:
    if n.count(char)==1:
        print("char is: ",char)
        break