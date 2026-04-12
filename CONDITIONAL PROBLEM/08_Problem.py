# pass strength checker: <6 char weak, 6-10 m ; >10 chars strong
p=input("enter your password: ")
l=int(len(p))
if l<6:
    sc="weak"
elif l<10:
    sc="medium"
else:
    sc="strong"
print("your password is ",sc)
