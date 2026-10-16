import json
import os

def add(name, number):
    number = str(number)

    if len(number) != 10 or not number.isdigit():
        print("Invalid Number! Please enter a valid number.")
        return

    filename = "database.json"
    data = []

    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = []

    for contact in data:
        if contact.get('name') == name:
            print(f"Error: The name '{name}' already exists in the database.")

        if contact.get('number') == number:
            print(f"Error: The number '{number}' already exists in the database.")

    data.append({"name": name, "number": number})

    with open(filename, "w") as f:
        json.dump(data, f)

    print(f"Successfully added {name} and {number} to the database...!")


def remove(name, number):
    number = str(number)

    if len(number) != 10 or not number.isdigit():
        print("Invalid Number! Please enter a valid 10-digit number.")
        return

    filename = "database.json"
    data = []

    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    contact_to_remove = {"name": name, "number": number}

    if contact_to_remove in data:
        data.remove(contact_to_remove)

        with open(filename, "w") as f:
            json.dump(data, f)

        print(f"Successfully removed {name} from the database!")
    else:
        print(f"Contact {name} with number {number} not found.")


while True:
    print("--- Phonebook Menu ---")
    print("1. Add")
    print("2. Search")
    print("3. Update")
    print("4. delete")
    print("5. View all")
    print("6. Exit")

    n = int(input("Enter your choice(1-6): "))

    match n:
        case 1:
            name = input("Enter your name: ").strip().lower()
            number = int(input("Enter your number: "))
            add(name, number)
        case 4:
            name = input("Enter your name: ").strip().lower()
            number = int(input("Enter your number: "))
            remove(name, number)
        case 6:
            print("Exiting...")
            break
        case _:
            print("Invalid Input! Please enter a valid choice.")