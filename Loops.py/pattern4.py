# num=int(input("Enter number "))
# for i in range(num,0,-1):
#      for j in range(i):
#          print("*",end=" ")
#      print()


# num=int(input("Enter number "))
# for i in range(num):
#      for j in range(num,i,-1):
#          print("*",end=" ")
#      print()

num=int(input("Enter number "))
for i in range(num):
     for j in range(i,num):
          print("*",end=" ")
     print()