age=int(input("Enter age "))
match age:
    case m if 0<=m<=2:
        print("infant")
    case m if 3<=m<=18:
        print("minor")
