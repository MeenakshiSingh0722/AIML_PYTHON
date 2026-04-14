# list uniqueness checker
i=["apple","banana","orange","apple","mango"]
unique=set()
for item in i:
    if item in unique:
        print("Duplicate ",item)
        break
    unique.add(item)