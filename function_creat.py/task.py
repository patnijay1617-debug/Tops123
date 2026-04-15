def student_details(roll_no,name,age):
    print(f"{roll_no}-{name}-{age}")

student_details(11,"shivam",20)
student_details(12,"jay",20)
r=int(input("Enter rollno "))
n=input("Enter name ")
a=int(input("Enter age "))
student_details(r,n,a)