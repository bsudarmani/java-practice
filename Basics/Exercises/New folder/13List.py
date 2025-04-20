
def display_menu():
    print("\n--- List Operations Menu ---")
    print("1. Add element")
    print("2. Insert element at specific index")
    print("3. Remove element")
    print("4. Update element at index")
    print("5. Sort the list")
    print("6. Display the list")
    print("7. Length of the list")
    print("8. Exit")

my_list = []

while True:
    display_menu()
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        item = input("Enter element to add: ")
        my_list.append(item)
        print("Element added.")

    elif choice == '2':
        item = input("Enter element to insert: ")
        try:
            index = int(input("Enter index to insert at: "))
            my_list.insert(index, item)
            print("Element inserted.")
        except:
            print("Invalid index.")

    elif choice == '3':
        item = input("Enter element to remove: ")
        if item in my_list:
            my_list.remove(item)
            print("Element removed.")
        else:
            print("Element not found in the list.")

    elif choice == '4':
        try:
            index = int(input("Enter index to update: "))
            if 0 <= index < len(my_list):
                new_item = input("Enter new value: ")
                my_list[index] = new_item
                print("Element updated.")
            else:
                print("Index out of range.")
        except:
            print("Invalid input.")

    elif choice == '5':
        my_list.sort()
        print("List sorted.")

    elif choice == '6':
        print("Current List:", my_list)

    elif choice == '7':
        print("Length of list:", len(my_list))

    elif choice == '8':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 8.")
