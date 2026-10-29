# empty dictionary
contacts = {}

while True:
    print('CONTACT MANAGEMENT SYSTEM')
    print('1. Create Contact')
    print('2. View all contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit')

    choice = input('Enter your choice:')

    # Implementation of condition
    if choice == '1':
        name = input('Enter contact to add:')
        if name in contacts:
            print(f'Contacts name {name} already exists.')
        else:
            age = input('Enter the age:')
            email = input('Enter the email:')
            mobile = input('Enter the mobile number:')
            contacts[name] = {'age': int(age), 'email':email, 'mobile':mobile}
            print(f'Contact name {name} has been created successfully!')

    elif choice == '2':
        name = input('Enter the contact name to view:')
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age: {age}, Mobile number: {mobile}')
        else:
            print('Contact not found!')

    elif choice == '3':
        name = input('Enter the name to update:')
        if name in contacts:
            name = input('Enter updated age:')
            email = input('Enter updated email:')
            mobile = input('Enter updated mobile number:')
            contacts[name] = {'age': int(age), 'email': email, 'mobile':mobile}
        else:
            print('Contact not found!')

    elif choice == '4':
        name = input('Enter the name to delete:')

        if name in contacts:
            del contacts[name]
            print(f'Contacts name {name} has been deleted successfully!')

        else:
            print('Contact not found!')

    elif choice == '5':
        search_name = input('Enter the contact name to search:')

        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found- Name:{name}, Age:{age}, Mobile number:{mobile}, Email:{email}')
                found = True

        if not found:
            print('No contact found with that name.')

    elif choice == '6':
        print(f'Total contact in your contact book: {len(contact)}')

    elif choice == '7':
        print('Ending program...Thank you for using!')
        break

    else:
        print('Invalid input! Please enter the correct input.')
