# movie ticket pricing
age=int(input("enter age: "))
day=input("enter day : ")
price= 12 if age>=18 else 8
if day== "wednesday" :
    price-=2
print("price will be $ ",price)