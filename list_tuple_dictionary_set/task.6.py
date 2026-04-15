shopping_lst=['Grocery','Dairy','Bakery']

print(f"Shopping list is as follows: {shopping_lst}")
while True:
    
    print(f"Choose an option from below: \n1)Add \n2)Update \n3)Delete \n4)Search \n5)Exit")
    user_choice=int(input("Enter your choice from the menu above: "))
    match user_choice:
        case 1:
    
            add=input("What do you want to add? ")
            shopping_lst.append(add) 
            print(shopping_lst)

        case 2:
            
          
            
            
            remove=input("what we have to reomove ")
            remove=remove.capitalize()
            index=shopping_lst.index(remove)

            shopping_lst.pop(index)

            addd=input("what u wnat to add ")
            shopping_lst.insert(index,addd)

            print(f"your updated item - {shopping_lst}")

        case 3:
            
             remove=input("what u want to delete ")  

             remove=remove.capitalize()
             index=shopping_lst.index(remove)

             shopping_lst.pop(index)
             print(f"after deletion your shopping list - {shopping_lst}")

        case 4:
            search=input("what u wnat to search ")
            search = search.capitalize()
            if search in shopping_lst:
                print(f"{search} is in the list ")
            
        case 5:
            break