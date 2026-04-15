# num=int(input("Enter number "))
# i=num
# while i>=1:
#     j=1
#     while j<=i:
#          print("*",end=" ")
#          j+=1
#     print()
#     i-=1
# i=2
# while i<=num:
#     j=1
#     while j<=i:
#          print("*",end=" ")
#          j+=1
#     print()
#     i+=1 



num=int(input("Enter number "))
for i in range(num*2-1):
     if(i<num):
         for j in range(i,num):
              print("*",end=" ")
         print()
     else:
          for j in range((i-num)+2):
               print("*",end=" ")
          print()
          