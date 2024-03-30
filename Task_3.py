class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address


class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name}: {contact.phone_number} , {contact.email}, {contact.address}")
        else:
            print("No contacts found.")

    def search_contact(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, new_contact):
        if 1 <= index <= len(self.contacts):
            self.contacts[index - 1] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            del self.contacts[index - 1]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")


def main():
    contact_list = ContactList()

    while True:
        print("\n1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_list.add_contact(contact)
        elif choice == '2':
            contact_list.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            found_contacts = contact_list.search_contact(query)
            if found_contacts:
                print("Search Results:")
                for contact in found_contacts:
                    print(f"{contact.name}: {contact.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            index = int(input("Enter index of contact to update: "))
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_list.update_contact(index, new_contact)
        elif choice == '5':
            index = int(input("Enter index of contact to delete: "))
            contact_list.delete_contact(index)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
