#tuple operations
def Search(tup,key):
    if key in tup:
        return "Element Found"
    return "Element not Found"
def Concat(l1,l2):
    return l1+l2

def repeat(l1,rep):
    return l1 * rep

def slice(tup,start ,end):
    return tup[start:end]


def isEmpty(tup):
    if len(tup) == 0:
        return True
    return False
def display(tup):
    if isEmpty(tup):
        print("Tuple is Empty")
        pass
    print("Tuple Elements")
    print(tup)
def main():
    try:
        print("\tTUPLE OPERATIONS")
        tup = (10,'munees',30,40.5)
        print("Press 1 for display")
        print("Press 2 for Repeat")
        print("Press 3 for Slice")
        print("Press 4 for Search")
        print("Press 5 for exit")
        while True:
            ch = int(input("Enter you choice:"))
            if ch == 1:
                display(tup)
            elif ch == 2:
                display(tup)
                rep = int(input("Enter a number:"))
                print(repeat(tup,rep))
            elif ch == 3:
                display(tup)
                s = int(input("Enter a starting value:"))
                e = int(input("Enter a ending value:"))
                print(f"Sliced tuple: {slice (tup,s,e)}")
            elif ch==4:
                display(tup)
                se = input("Enter a element to search:")
                print(Search(tup,se))
            elif ch == 5:
                break
            else:
                print("Invalid Choice")
    except ValueError as e:
            print(f"Error: {e}")
main()
