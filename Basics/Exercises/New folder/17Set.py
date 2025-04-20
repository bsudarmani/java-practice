
def display_menu():
    print("\n--- Set Operations Menu ---")
    print("1. Create two sets")
    print("2. Remove an element from a set")
    print("3. Display both sets")
    print("4. Union of sets")
    print("5. Intersection of sets")
    print("6. Difference (Set1 - Set2, Set2 - Set1)")
    print("7. Symmetric Difference")
    print("8. Exit")

# Initialize empty sets
set1 = set()
set2 = set()

while True:
    display_menu()
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        set1 = set(input("Enter elements for Set 1 (space-separated): ").split())
        set2 = set(input("Enter elements for Set 2 (space-separated): ").split())
        print("Both sets created.")

    elif choice == '2':
        sel = input("From which set? (1 or 2): ")
        item = input("Enter element to remove: ")
        target_set = set1 if sel == '1' else set2
        if item in target_set:
            target_set.remove(item)
            print(f"{item} removed from Set {sel}.")
        else:
            print("Element not found in the selected set.")

    elif choice == '3':
        print("Set 1:", set1)
        print("Set 2:", set2)

    elif choice == '4':
        print("Union:", set1.union(set2))

    elif choice == '5':
        print("Intersection:", set1.intersection(set2))

    elif choice == '6':
        print("Set1 - Set2:", set1.difference(set2))
        print("Set2 - Set1:", set2.difference(set1))

    elif choice == '7':
        print("Symmetric Difference:", set1.symmetric_difference(set2))

    elif choice == '8':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 8.")
