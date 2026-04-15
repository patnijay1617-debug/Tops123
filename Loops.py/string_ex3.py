contact_number=input("Enter contact number ")
if contact_number.startswith("91") and len(contact_number)==12:
    print(f"{contact_number} is valid number ")
else:
    print(f"{contact_number} is invalid ")