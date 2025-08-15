FILENAME = "contact.txt"

# Load contacts from file
def load_contacts():
    contacts = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts.append({"name": name, "phone": phone, "email": email})
    except FileNotFoundError:
        pass
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        for c in contacts:
            file.write(f"{c['name']}, {c['phone']}, {c['email']}\n")

# Add a new contact
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    if not name:
        print("Name is required.")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added!")

# View all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for idx, c in enumerate(contacts, start=1):
        print(f"{idx}. {c['name']} | {c['phone']} | {c['email']}")

# Main program
if __name__ == "__main__":
    contacts = load_contacts()

    while True:
        print("\n1. View contacts")
        print("2. Add contact")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            view_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
