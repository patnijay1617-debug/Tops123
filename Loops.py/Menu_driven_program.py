while True:
    print("\n1. factorial\n2. count Digit\n3. Sum of Digits\n4. Prime number\n5. exit ")
    choice=int(input("Enter choice "))
    match choice:
       case 1:
          num=int(input("Enter your factorial number "))
          fact=1
          for i in range(1,num+1):
            fact=fact*i
          print(f"factorial of {num} is {fact}")
       case 2:
          num=int(input("Enter your number "))
          count=0
          num1=num
          while num!=0:
             rem=num%10
             print("rem = ",rem )
             count+=1
             num=num//10
             print("count = ", num)
          print(f"{num1} contains = {count} digits ")
       case 3:
          num=int(input("Enter number "))
          sum=0
          for i in range(1,num+1):
             sum=sum+i

          print(f"sum of {num} is {sum}")
       case 4:
          num=int(input("Enter number "))
          for i in range(2,num):
              if num%i==0:
                  print(f"{num} is not prime")
                  break
              else:
                  print(f"{num} is prime ")
       case 5:
          break
       case _:
          print("invalid choice")

          





          
