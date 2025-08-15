from cmath import phase

FILENAME = "contact.txt"
def load_contacts():
    contact = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contact.append({"name": name, "phone": phone, "email": email})
    except FileNotFoundError:
        pass
    return contact
def save_contacts(contact):
    with open (FILENAME, "w") as file:
        for c in contact:
            file.write(f"{c['name']}, {c['phone']}, {c['email']}\n")
if __name__ == "__main__":
    test = [{"name": "Alice", "phone": "01234567", "email": "a@gmail.com"}]
    save_contacts(test)
    print(load_contacts())

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    if not name:
        print("Name is required."); return
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts found."); return
    for idx, c in enumerate(contacts, start=1):
        print(f"{idx}. {c['name']} | {c['phone']} | {c['email']}")
