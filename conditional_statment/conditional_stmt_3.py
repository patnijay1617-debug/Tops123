age=int(input("Enter age "))
if age>=18:
    weight=int(input("Enter Weight "))
    if weight>=55:
        print("user can donete blood")
    else:
        print("due to underweight user can not donate blood")
else:
    print("Due to age user can not donate blood")
        