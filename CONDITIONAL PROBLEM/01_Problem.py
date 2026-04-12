#print senior adult child and all based on age
age=int(input("enter a age: "))
if age<13:
    print("Child")
elif age<20 :
    print("Teenager")
elif age<60:
    print("Adult")
else :
    print("Senior")