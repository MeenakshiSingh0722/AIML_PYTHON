# multiplication table
n=int(input("enter a num: "))
for i in range(1,11):
    if n==5:
        continue
    print(n, ' X',i,' =',n*i)