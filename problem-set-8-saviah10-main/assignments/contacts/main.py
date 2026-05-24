# TODO: your code here!
# i am so close but there is an error with the add number function!!
def addnumber(contacts):
    name = input("Contact name?\n")
    number = input("Phone number?\n")
    if name not in contacts:
        # use a set or list???
        contacts [name] = set()
        contacts[name].add(number)
        print(f"Added number: {number} for {name}")

# nts- make delete funtion w/ name input and if stmt.
def deletenumber(contacts):
    name = input("Contact name?\n")
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}")
    else:
        print("Name not found. Try again.")

# nts - print contact w function that just retrieves the name from contacts??
def printcontact(contacts):
    name = input("Contact name?\n")
    if name in contacts:
        print(f'Contact "{name}":')
        print("Phone numbers:")
        # nts - sort it so thats its the right order
        for number in sorted(contacts[name]):
            print(number)
    else:
        print("Name not found. Try again.")

def printnamewithmost(contacts):
    # nts - gonna have to iterate over the contacts to find max i think
    maxnum = 0
    maxcon = None
    for name, numbers in contacts.items():
        if len(numbers) > maxnum:
            maxcon = name
            maxnum = len(numbers)
            # create if statement?? for number to print sorted
    if maxcon:
        print(f'Contact with most phone numbers: {maxcon}')
        for number in sorted(contacts[maxcon]):
            print(f"Phone numbers: {number}")

def contactsapp():
    contacts = {}
    print("Welcome to the contacts app!\n")
    while True:
        print("1. Add a phone number")
        print("2. Delete a contact")
        print("3. Print a contact")
        print("4. Print contact with most phone numbers")
        print("5. Quit")
        selected = input("What would you like to do?\n")
            
        if selected == "1":
                addnumber(contacts)
        elif selected == "2":
                deletenumber(contacts)
        elif selected == "3":
                printcontact(contacts)
        elif selected == "4":
                printnamewithmost(contacts)
        elif selected == "5":
                print("Bye!")
                break
        else:
            print("Invalid choice, try again")

contactsapp()