# transportation mode selection
d=int(input("enter distance : "))
if d<3:
    t="walk"
elif d<=15:
    t="bike"
else :
    t="car"
print("your mode of transport should be: ",t)