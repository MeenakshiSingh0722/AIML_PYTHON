# pet food recommendation
p=input("enter your pet :")
a=int(input("enter age of your pet: "))

if(p=="dog"):
    if(a<2): r="puppy food"
    else : r="adult food"
elif (p=="cat"):
    if(a>=5): r="senior food"
    else : r="kitten food"
print("your ",p," food should be ",r)