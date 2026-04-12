#leap year divisible by 4 or not
y=int(input("enter your year to check: "))
if(y% 400 == 0)or (y%4==0 and 100!=0):
    print(y," year is leap year")
else:
    print(y," year not a leap year")

