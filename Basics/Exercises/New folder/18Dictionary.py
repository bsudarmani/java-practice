
def display_menu():
    print("\n--- Dictionary Operations Menu ---")
    print("1. Create a new dictionary")
    print("2. Add a key-value pair")
    print("3. Update a value for a key")
    print("4. Remove a key")
    print("5. Display the dictionary")
    print("6. Search for a key")
    print("7. Get all keys")
    print("8. Get all values")
    print("9. Get all items")
    print("10. Exit")

# Initialize empty dictionary
my_dict = {}

while True:
    display_menu()
    choice = input("Enter your choice (1-10): ")

    if choice == '1':
        n = int(input("How many key-value pairs do you want to add? "))
        for _ in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
        print("Dictionary created.")

    elif choice == '2':
        key = input("Enter key to add: ")
        value = input("Enter value: ")
        my_dict[key] = value
        print("Key-value pair added.")

    elif choice == '3':
        key = input("Enter key to update: ")
        if key in my_dict:
            new_value = input("Enter new value: ")
            my_dict[key] = new_value
            print("Value updated.")
        else:
            print("Key not found.")

    elif choice == '4':
        key = input("Enter key to remove: ")
        if key in my_dict:
            del my_dict[key]
            print("Key removed.")
        else:
            print("Key not found.")

    elif choice == '5':
        print("Current Dictionary:", my_dict)

    elif choice == '6':
        key = input("Enter key to search: ")
        if key in my_dict:
            print(f"{key} found with value: {my_dict[key]}")
        else:
            print("Key not found.")

    elif choice == '7':
        print("Keys:", list(my_dict.keys()))

    elif choice == '8':
        print("Values:", list(my_dict.values()))

    elif choice == '9':
        print("Items (key-value pairs):", list(my_dict.items()))

    elif choice == '10':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 10.")
