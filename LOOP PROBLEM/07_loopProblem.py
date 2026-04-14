# # keep asking the user for ip until they enter a num between 1 and 100
while True:
    n=int(input("Enter a num between 1 and 10"))
    if 1<= n <=10:
        print("thanxx")
        break
    else:
        print("invalid num try again")