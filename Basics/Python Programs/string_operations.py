def stringAppend(s1, s2):
    return s1 + s2

def stringRemove(s, sub):
    return s.replace(sub, "")

def stringSearch(s, key):
    if key in s:
        return "Substring Found"
    return "Substring not Found"

def stringFind(s, sub):
    return s.find(sub)

def stringCount(s, sub):
    return s.count(sub)

def stringRepeat(s, rep):
    return s * rep

def stringSlice(s, start, end):
    return s[start:end]

def stringLength(s):
    return len(s)

def stringToUpper(s):
    return s.upper()

def stringToLower(s):
    return s.lower()

def isEmpty(s):
    if len(s) == 0:
        return True
    return False

def display(s):
    if isEmpty(s):
        print("String is Empty")
        return
    print("String Content:")
    print(s)

def main():
    try:
        print("\tSTRING OPERATIONS")
        s = ""
        print("Press 1 to input string")
        print("Press 2 to display string")
        print("Press 3 to append string")
        print("Press 4 to remove substring")
        print("Press 5 to repeat string")
        print("Press 6 to slice string")
        print("Press 7 to search substring")
        print("Press 8 to get length")
        print("Press 9 to convert to uppercase")
        print("Press 10 to convert to lowercase")
        print("Press 11 to find substring index")
        print("Press 12 to count substring occurrences")
        print("Press 13 to exit")
        while True:
            ch = int(input("Enter your choice:"))
            if ch == 1:
                s = input("Enter a string:")
                display(s)
            elif ch == 2:
                display(s)
            elif ch == 3:
                s2 = input("Enter a string to append:")
                s = stringAppend(s, s2)
                display(s)
            elif ch == 4:
                sub = input("Enter a substring to remove:")
                s = stringRemove(s, sub)
                print(f"After removing '{sub}': {s}")
            elif ch == 5:
                rep = int(input("Enter number of repetitions:"))
                print(stringRepeat(s, rep))
            elif ch == 6:
                start = int(input("Enter start index:"))
                end = int(input("Enter end index:"))
                print(f"Sliced String: {stringSlice(s, start, end)}")
            elif ch == 7:
                key = input("Enter a substring to search:")
                print(stringSearch(s, key))
            elif ch == 8:
                print(f"Length of string: {stringLength(s)}")
            elif ch == 9:
                print(f"Uppercase: {stringToUpper(s)}")
            elif ch == 10:
                print(f"Lowercase: {stringToLower(s)}")
            elif ch == 11:
                sub = input("Enter a substring to find:")
                index = stringFind(s, sub)
                if index != -1:
                    print(f"Substring found at index {index}")
                else:
                    print("Substring not found")
            elif ch == 12:
                sub = input("Enter a substring to count:")
                print(f"'{sub}' occurred {stringCount(s, sub)} times")
            elif ch == 13:
                break
            else:
                print("Invalid Choice")
    except ValueError as e:
        print(f"Error: {e}")

main()
