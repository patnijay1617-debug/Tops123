marks=int(input("Enter marks "))
match marks:
    case m if 70<=m<=100:
        print("A")
    case m if 60<=m<=69:
        print("B")
    case m if 45<=m<=59:
        print("C")
    case _:
        print("fail")
