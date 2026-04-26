#Contact Book program Ver 1

contacts = {} # Used for adding contacts 
 
while True:  #Created a loop to display the menu or whatever idk
    print("1. Add Contacts")
    print("2. Edit Contacts")
    print("3. View Contacts")
    print("4. Search Contacts")
    print("5. Delete Contacts")
    print("6. Exit")
    choice = input("Enter a choice: ")
    if choice == "1": #This choice just lets u add contacts as simple as that 

        name = input("Enter a name: ")
        number = input("Enter a number: ")
        contacts[name] = number

    elif choice == "2": #This choice is obvious as f that its used to edit the contacts or whatever 
        old_name = input("Enter the old name u want to update: ")
        if old_name in contacts:
            new_name = input("Enter a new name: ")
            new_number = input("Enter a new number: ")
            del contacts[old_name] #Cause dict doesnt remove values on its own 
            contacts[new_name] = new_number

            print("Successful")

        else:
            print("Contact not found are u an idiot ?!")

    elif choice == "3": #The third choice huh it just displays whatever u added
        for name, number in contacts.items():
            print(name,":",number)

    elif choice == "4": #This choice is for number searching obviously 
        searchname = input("Enter a name for search: ")
        if searchname in contacts:
            print(f"Number: {contacts[name]}")
        else:
            print("Not found !!")

    elif choice == "5": #Finally at the choice where we can delete a contact or some shit
        deletename = input("Enter a contact for deletion: ")
        if deletename in contacts:
            del contacts[name]
            print("Done successfully !!")

        else:
            print("U CANT DELETE A CONTACT U HAVENT ADDED DUMASS !!")
    
    else: #just type 6 or sm shi to exit finally jeez
        break

print("Thx for using this contact program !!")