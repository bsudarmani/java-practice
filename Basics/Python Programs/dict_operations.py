def getDataByType(ty):
    if ty == 'i':
        return int(input("Enter a value (integer): "))
    elif ty == 'f':
        return float(input("Enter a value (float): "))
    elif ty == 's':
        return input("Enter a value (string): ")
    else:
        return input("Enter a value (default string): ")

def getKeyType(ty):
    if ty == 'i':
        return int(input("Enter a key (integer): "))
    elif ty == 's':
        return input("Enter a key (string): ")
    else:
        return input("Enter a key (default string): ")

def createDict(d):
    n = int(input("Enter the number of elements: "))
    print("Type Mode:\nInteger - i\nFloat - f\nString - s")
    for _ in range(n):
        kty = input("Enter the type of the key (i/s): ").strip().lower()
        key = getKeyType(kty)
        vty = input("Enter the type of the value (i/f/s): ").strip().lower()
        d[key] = getDataByType(vty)

def updateDict(d):
    print("\tUPDATE DICTIONARY")
    print("Type Mode:\nInteger - i\nFloat - f\nString - s")
    kty = input("Enter the type of the key (i/s): ").strip().lower()
    key = getKeyType(kty)
    if key in d:
        vty = input("Enter the type of the new value (i/f/s): ").strip().lower()
        d[key] = getDataByType(vty)
        return "Update Successful"
    else:
        return "Key not found"

def deleteDict(d):
    print("\tDELETE DICTIONARY")
    print("Type Mode:\nInteger - i\nFloat - f\nString - s")
    kty = input("Enter the type of the key (i/s): ").strip().lower()
    key = getKeyType(kty)
    if key in d:
        del d[key]
        return "Key deleted successfully"
    else:
        return "Key not found"

def searchDict(d):
    print("\tSEARCH DICTIONARY")
    print("Type Mode:\nInteger - i\nFloat - f\nString - s")
    vty = input("Enter the type of the value (i/f/s): ").strip().lower()
    value = getDataByType(vty)
    for k, v in d.items():
        if v == value:
            return f"Element found, its key is: {k}"
    return "Element not found"

def insertDict(d):
    print("\tINSERT INTO DICTIONARY")
    print("Type Mode:\nInteger - i\nFloat - f\nString - s")
    kty = input("Enter the type of the key (i/s): ").strip().lower()
    key = getKeyType(kty)
    
    if key in d:
        print("Key already exists. Use Update if you want to change the value.")
        return
    
    vty = input("Enter the type of the value (i/f/s): ").strip().lower()
    value = getDataByType(vty)
    d[key] = value
    print("Element inserted successfully.")


def displayDict(d):
    if not d:
        print("Dictionary is empty")
    else:
        print("Dictionary contents:")
        for k, v in d.items():
            print(f"{k}: {v}")

def dictMain():
    try:
        d = {}
        while True:
            print("\n\tDICTIONARY OPERATIONS")
            print("1. Create Dictionary")
            print("2. Display Dictionary")
            print("3. Insert into Dictionary")
            print("4. Update Dictionary")
            print("5. Delete from Dictionary")
            print("6. Search in Dictionary")
            print("7. Exit")

            ch = int(input("Enter your choice: "))
            if ch == 1:
                createDict(d)
            elif ch == 2:
                displayDict(d)
            elif ch == 3:
                insertDict(d)
            elif ch == 4:
                res = updateDict(d)
                print(res)
            elif ch == 5:
                res = deleteDict(d)
                print(res)
            elif ch == 6:
                res = searchDict(d)
                print(res)
            elif ch == 7:
                print("Exiting Dictionary Operations")
                break
            else:
                print("Invalid choice. Try again.")
    except ValueError as ve:
        print(f"Error: {ve}")

dictMain()
