print("1. Addition\n2. Substraction\n3. Muplication\n4. Division")
choice=int(input("Enter choise "))
no1=int(input("Enter no1 "))
no2=int(input("Enter no2 "))
# if choice==1:
#     print(f"Addition {no1+no2}")
# elif choice==2:
#     print(f"Substraction {no1-no2}")
# elif choice==3:
#     print(f"Multilication {no1*no2}")
# elif choice==4:
#     print(f"Division {no1/no2}")
# else:
#     print("Invalid number ")

match choice:
    case 1:
        print(f"Addition {no1+no2}")
    case 2:
        print(f"Substraction {no1-no2}")
    case 3:
        print(f"Multilication {no1*no2}")
    case 4:
        print(f"Divition {no1/no2}")
    case _:
        print("Invalid number ")
        


