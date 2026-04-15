name=input("Enter name ")
i=name.count("is")
print(f"{name} contains {i} is latter ")
print(f"total string lenght is {len(name)}")

ans=name.split()
print(len(ans))

for i in ans:
    print(f"{i} contains --->{i.count('a')} a latter")
