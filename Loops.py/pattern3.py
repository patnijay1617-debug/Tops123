num=int(input("Enter num "))

for i in range(num):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()