name=input("Enter name ")
count=0
for i in range(len(name)):
    print(f"{i}--->{name[i]}")
    if name[i]=='a':
        count+=1
print(f"count of a is {count}")