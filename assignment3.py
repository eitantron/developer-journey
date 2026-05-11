

def show_menu():
    print("\n=== Contact book ")
    print(" Add contact")
    print("2. View all contacts")
    print("3 Search contact by name")
    print("4 Delete contact")
    print("5. Quit")


def add_contact(contacts):
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    tags_text = input("Tags (comma-separated, e.g. friend,gym): ").strip()
    tags = [t.strip() for t in tags_text.split(",") if t.strip()]

    if name in contacts:
        overwrite = input(f'"{name}" already exists. Overwrite? (y/n): ').strip().lower()
        if overwrite != "y":
            print("Cancelled.")
            return

    contacts[name] = {
        "phone": phone,
        "email": email,
        "tags": tags,
    }
    print(f"Saved contact: {name}")


def view_contacts(contacts):
    if not contacts:
        print("No contacts yet.")
        return

    for name, info in contacts.items():
        tags_str = ", ".join(info["tags"]) if info["tags"] else "(none)"
        print(f"\n{name}")
        print(f"  phone: {info['phone']}")
        print(f"  email: {info['email']}")
        print(f"  tags:  {tags_str}")


def search_contact(contacts):
    name = input("Name to search: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    if name not in contacts:
        print("Contact not found.")
        return

    info = contacts[name]
    tags_str = ", ".join(info["tags"]) if info["tags"] else "(none)"
    print(f"\n{name}")
    print(f"  Phone: {info['phone']}")
    print(f"  Email: {info['email']}")
    print(f"  Tags:  {tags_str}")


def delete_contact(contacts):
    name = input("Name to delete: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    if name not in contacts:
        print("Contact not found.")
        return

    del contacts[name]
    print(f"Deleted: {name}")


def main():
    contacts = {}

    while True:
        show_menu()
        choice = input("Pick 1-5: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
