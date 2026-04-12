# #print senior adult child and all based on age
# age=int(input("enter a age: "))
# if age<13:
#     print("Child")
# elif age<20 :
#     print("Teenager")
# elif age<60:
#     print("Adult")
# else :
#     print("Senior")

# movie ticket pricing
# age=int(input("enter age: "))
# day=input("enter day : ")
# price= 12 if age>=18 else 8
# if day== "wednesday" :
#     price-=2
# print("price will be $ ",price)

# grade calculator
# marks=int(input("entre marks: "))
# if marks >=101:
#     print ("plz verify your marks ")
#     exit()
# if marks>=90:
#     grade="A"
# elif marks >=80:
#     grade="B"
# elif marks >=70:
#     grade="c"
# elif marks >=60:
#     grade="d"
# else :
#     grade="e"
# print("grade is : ", grade)

# # fruit ripeness
# fruit="Banana"
# color="yellow"
# if(fruit =="Banana"):
#     if color=="green":
#         print("unripe")
#     elif color=="yellow":
#         print("ripe")
#     elif color=="brown":
#         print("overripe")

# #weather activity suggestion
# w=input("enter a weather: ")
# if w =="sunny":
#     activity ="go for a walk"
# elif w=="rainy ":
#     activity ="read a book"
# elif w=="snowy":
#     activity ="build a snowman"
# print(activity)

# transportation mode selection
# d=int(input("enter distance : "))
# if d<3:
#     t="walk"
# elif d<=15:
#     t="bike"
# else :
#     t="car"
# print("your mode of transport should be: ",t)

#customize a coffee order s ,m, l with an option for extra shot of espresso
# os=input("enter size: ")
# es=bool(input("enter true or false: "))
# if es:
#     coffee= os+"coffee with an extra shot"
# else :
#     coffee= os+"coffee"
# print("order: ",coffee)

# pass strength checker: <6 char weak, 6-10 m ; >10 chars strong
# p=input("enter your password: ")
# l=int(len(p))
# if l<6:
#     sc="weak"
# elif l<10:
#     sc="medium"
# else:
#     sc="strong"
# print("your password is ",sc)

#leap year divisible by 4 or not
# y=int(input("enter your year to check: "))
# if(y% 400 == 0)or (y%4==0 and 100!=0):
#     print(y," year is leap year")
# else:
#     print(y," year not a leap year")

#pet food recommendation
# p=input("enter your pet :")
# a=int(input("enter age of your pet: "))
#
# if(p=="dog"):
#     if(a<2): r="puppy food"
#     else : r="adult food"
# elif (p=="cat"):
#     if(a>=5): r="senior food"
#     else : r="kitten food"
# print("your ",p," food should be ",r)