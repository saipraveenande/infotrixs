import json


def getNumber():
    while True:
        try:
            number= int(input("Enter number without extensions:"))
            if len(str(number)) == 10:
                break
            else:
                print("Please, enter valid 10 digit mobile number")
        except ValueError:
            print("Please, enter valid 10 digit mobile number")
    return number


def getMail():
    while True:
        email = input("Enter mail ID:")
        if (('@' in email) and ('.' in email)):
            break
        else:
            print("Please enter valid email address:")
    return email


def saveContact(contactList, contactFile):
    with open(contactFile, 'w') as file:
        json.dump(contactList, file)


def addContact(contactList, contactFile):
    while True:
        name = input("Enter name:")
        if name not in contactList:
            contactList[name] = {}
            contactList[name]["Phone"] = getNumber()
            contactList[name]["Mail"] = getMail()
            saveContact(contactList, contactFile)
            print(f"{name} contact was added!")
            break
        else: 
            print(f"{name} is already existed. Please save with another name.")


def searchContact(contactList):
    while True:
        name = input("Enter name to search: ")
        if name in contactList:
            print(f"Name    : {name}")
            print(f"Number  : {contactList[name]['Phone']}")
            print(f"Mail ID : {contactList[name]['Mail']}")
            break
        else:
            print(f"{name} is not saved in your contacts")


def updateContact(contactList, contactFile):
    name = input("Enter name to update the contact details: ")
    if name in contactList:
        while True:
            print("----------------------------------------------------")
            print("       Choose one option to update:")
            print("        1. To update name")
            print("        2. To update number")
            print("        3. To update mail")
            print("        4. To update both number and mail")
            print("        Press any othee key to go to Main Menu")
            print("----------------------------------------------------")

            option = input("Enter something to update: ")
            match option:
                case '1':
                    newName = input("Enter new name for same number and mail id:")
                    contactList[newName] = contactList[name]
                    del contactList[name]
                    # ContactList[newName] = ContactList.pop(name)
                    saveContact(contactList, contactFile)
                    print(f"{name} is updated to {newName}")

                case '2':
                    contactList[name]['Phone'] = getNumber()
                    saveContact(contactList, contactFile)
                    print(f"{name}'s Mobile number was updated")

                case '3':
                    contactList[name]['Mail'] = getMail()
                    saveContact(contactList, contactFile)
                    print(f"{name}'s Mail ID was updated")
                
                case '4':
                    contactList[name]['Phone'] = getNumber()
                    contactList[name]['Mail'] = getMail()
                    saveContact(contactList, contactFile)
                    print(f"{name}'s Mobile number and Mail ID was updated")

                case _:
                    break
    
    else:
        print(f"{name} is not saved in your contacts. Please enter valid one.")
        updateContact(contactList)    


def deleteContact(contactList, contactFile):
    name = input("Enter name to delete the contact: ")
    if name in contactList:
        del contactList[name]
        saveContact(contactList, contactFile)
        print(f"{name} contact details are deleted!")
    else:
        print(f"{name} is not in your contacts")


def displayContact(contactList):
    serial_number= 1
    s_sno = "  "
    print("--------+----------------+------------+------------------------")
    print("   SNo  | Name           | Number     | Mail id  ")
    print("--------+----------------+------------+------------------------")
    for i in contactList:
        s_name = (14 - len(i)) * " " 
        print( f"{s_sno} {serial_number}    | {i}{s_name} | {contactList[i]['Phone']} | {contactList[i]['Mail']} ")
        serial_number += 1
        if s_sno ==10:
            s_sno = " "
    print("--------+----------------+------------+------------------------")
    print("")


def main():
    contactFile = 'contacts.json'
    try:
        with open(contactFile, 'r') as file:
            contactList = json.load(file)
    except FileNotFoundError:
        contactList = {}


    print("---------------------------------------------------------------------------------------")
    print("                     || Welcome to Contact Management System ||")

    while True:
        print("---------------------------------------------------------------------------------------")
        print("    Choose an option below ")
        print("")
        print("     1. Add new contact")
        print("     2. Search for existing contact details")
        print("     3. Update existing contact")
        print("     4. Delete contact")
        print("     5. Display contacts")
        print("     Press other key to exit from the application")
        print("---------------------------------------------------------------------------------------")

        option = input("         Enter your option ==> ")

        match option:
            case "1":
                addContact(contactList, contactFile)
            case "2":
                searchContact(contactList)
            case "3":
                updateContact(contactList, contactFile)
            case "4":
                deleteContact(contactList, contactFile)
            case "5":
                displayContact(contactList)
            case _:
                break

    print("---------------------------------------------------------------------------------------")
    print("                    Thank you for using Contact Management System!! ")
    print("---------------------------------------------------------------------------------------") 


if __name__ == "__main__":
    main()

