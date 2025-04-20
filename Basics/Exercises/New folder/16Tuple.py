
def display_menu():
    print("\n--- Tuple Operations ---")
    print("1. Create a new tuple")
    print("2. Display the tuple")
    print("3. Access element by index")
    print("4. Slice the tuple")
    print("5. Search for an element")
    print("6. Index of an element")
    print("7. Length of the tuple")
    print("8. Exit")

# Initial empty tuple
my_tuple = ()

while True:
    display_menu()
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        items = input("Enter elements separated by spaces: ")
        my_tuple = tuple(items.split())
        print("Tuple created.")

    elif choice == '2':
        print("Current Tuple:", my_tuple)

    elif choice == '3':
        try:
            index = int(input("Enter index to access: "))
            print("Element at index", index, ":", my_tuple[index])
        except:
            print("Invalid index.")

    elif choice == '4':
        try:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced Tuple:", my_tuple[start:end])
        except:
            print("Invalid input for slicing.")

    elif choice == '5':
        element = input("Enter element to search: ")
        if element in my_tuple:
            print(f"{element} is in the tuple.")
        else:
            print(f"{element} is not in the tuple.")



    elif choice == '6':
        element = input("Enter element to find index of: ")
        if element in my_tuple:
            print(f"Index of {element}:", my_tuple.index(element))
        else:
            print(f"{element} not found in the tuple.")

    elif choice == '7':
        print("Length of the tuple:", len(my_tuple))

    elif choice == '8':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 8.")
