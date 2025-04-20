text = input("Enter a string: ")

print("\n1. Remove Extra Spaces")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Count Words")
print("5. Reverse Words")
print("6. Check if Palindrome")
print("7. Exit")

while True:
    choice = input("\nChoose an option (1-7): ")

    if choice == "1":
        text = " ".join(text.split())
        print("Processed Text:", text)

    elif choice == "2":
        print("Uppercase Text:", text.upper())

    elif choice == "3":
        print("Lowercase Text:", text.lower())

    elif choice == "4":
        word_count = len(text.split())
        print("Word Count:", word_count)

    elif choice == "5":
        reversed_text = " ".join(text.split()[::-1])
        print("Reversed Words:", reversed_text)

    elif choice == "6":
        clean_text = text.replace(" ", "").lower()
        is_palindrome = clean_text == clean_text[::-1]
        print("Is Palindrome?", is_palindrome)

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please select a valid option.")