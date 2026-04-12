#customize a coffee order s ,m, l with an option for extra shot of espresso
os=input("enter size: ")
es=bool(input("enter true or false: "))
if es:
    coffee= os+"coffee with an extra shot"
else :
    coffee= os+"coffee"
print("order: ",coffee)
