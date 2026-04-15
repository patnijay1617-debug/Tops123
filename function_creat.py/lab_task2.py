def check_number(num):
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not prime")
            break  
    else:
        print(f"{num} is prime ")
        

no=int(input("Enter number "))
check_number(no)