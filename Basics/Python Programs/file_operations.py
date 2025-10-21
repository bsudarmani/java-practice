import os

# ---------- File Operations ----------

def createFile(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            pass
        print(f"File '{filename}' created successfully.")
    else:
        print(f"File '{filename}' already exists.")

def writeToFile(filename, data):
    with open(filename, "w") as f:
        f.write(data)
    print(f"Data written to file '{filename}' successfully.")

def appendToFile(filename, data):
    with open(filename, "a") as f:
        f.write(data)
    print(f"Data appended to file '{filename}' successfully.")

def readFromFile(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            if content.strip() == "":
                print("File is empty.")
            else:
                print("\n--- FILE CONTENT ---")
                print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found!")

def deleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"File '{filename}' not found!")

def renameFile(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}'.")
    else:
        print(f"File '{old_name}' not found!")

# ---------- Main Program ----------

def main():
    while True:
        print("\n--- FILE OPERATIONS MENU ---")
        print("1. Create File")
        print("2. Write to File")
        print("3. Read from File")
        print("4. Append to File")
        print("5. Delete File")
        print("6. Rename File")
        print("7. Exit")

        try:
            ch = int(input("Enter your choice: "))
            if ch == 7:
                print("Exiting program...")
                break

            filename = input("Enter filename: ")

            if ch == 1:
                createFile(filename)
            elif ch == 2:
                data = input("Enter text to write into the file:\n")
                writeToFile(filename, data)
            elif ch == 3:
                readFromFile(filename)
            elif ch == 4:
                data = input("Enter text to append into the file:\n")
                appendToFile(filename, data)
            elif ch == 5:
                deleteFile(filename)
            elif ch == 6:
                new_name = input("Enter new filename: ")
                renameFile(filename, new_name)
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number.")

# Run the program
main()
