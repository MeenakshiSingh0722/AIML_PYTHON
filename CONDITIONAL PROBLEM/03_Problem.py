# grade calculator
marks=int(input("entre marks: "))
if marks >=101:
    print ("plz verify your marks ")
    exit()
if marks>=90:
    grade="A"
elif marks >=80:
    grade="B"
elif marks >=70:
    grade="c"
elif marks >=60:
    grade="d"
else :
    grade="e"
print("grade is : ", grade)