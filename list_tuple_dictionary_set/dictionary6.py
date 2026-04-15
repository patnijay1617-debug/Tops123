emp_data={
    101:{"name":"divya","email":"divya@gmail.com","salary":20000},
    102:{"name":"jay","email":"jay@gmail.com","salary":25000},
    103:{"name":"shivam","email":"shivam@gmail.com","salary":22000},
    104:{"name":"dharmishtha","email":"dharmishtha","salary":30000}
    }
while True:
    print("1. add Employe")
    print("2. search Employe")
    print("3. Display all Employe")
    print("4. update employe")
    print("exit")
    choice=int(input("Enter choice "))
    match choice:
        case 1:
            eid=int(input("Enter eid "))
            ename=input("Enter name ")
            email=input("Enter email")
            esalary=int(input("Enter salary "))
            emp_data[eid]={"name":ename,"email":email,"salary":esalary,}
            print("Employe added succesfully ")
        case 2:
            search_id=int(input("Enter emp id "))
            if search_id in emp_data.keys():
                print(emp_data[search_id])
            else:
                print(f"{search_id} is unvalid ")
        case 3:
            for k,v in emp_data.items():
                print(k)
                for i in v.items():
                    print("\t",i)
        case 4:
            search_id=int(input("Enter emp id "))
            if search_id in emp_data.keys():
                new_salary=int(input("Enter updated salary "))
                for k,v in emp_data.items():
                    if k==search_id:
                        v["salary"] = new_salary
            print("salary updated succesfully ")        
        case 5:break
        