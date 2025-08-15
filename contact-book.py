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