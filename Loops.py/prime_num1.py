num=int(input("Enter number "))
i=2
while i<num:
    if num%i==0:
        print(f"{num} is not prime ")
        break
    i+=1
else:
    print(f"{num} is prime")
    