email=input("Enter email ")
# print(email.endswith("@gmail.com"))
if email.endswith("@gmail.com"):
    print(f"{email} is valid email address ")
else:
    print(f"{email} is invalid email address ")