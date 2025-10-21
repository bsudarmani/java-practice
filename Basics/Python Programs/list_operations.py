#list operations
def listAppend(lst,val):
    lst.append(val)

def Remove(lst,val):
    l = []
    for i in lst:
        if i != val:
            l.append(i)
    return l

def Search(lst,key):
    if key in lst:
        return "Element Found"
    return "Element not Found"
def Concat(l1,l2):
    return l1+l2

def repeat(l1,rep):
    return l1 * rep

def slice(lst,start ,end):
    return lst[start:end]

def get(lst,size):
    for i in range(0,size):
        lst[i] = input(f"Enter element {i+1}:")
def isEmpty(lst):
    if len(lst) == 0:
        return True
    return False
def display(lst):
    if isEmpty(lst):
        print("List is Empty")
        return
    print("List Elements")
    print(lst)
def main():
    try:
        print("\tLIST OPERATIONS")
        lst = []
        print("Press 1 for insert")
        print("Press 2 for display")
        print("Press 3 for Remove")
        print("Press 4 for Concat")
        print("Press 5 for Repeat")
        print("Press 6 for Slice")
        print("Press 7 for Search")
        print("Press 8 for exit")
        while True:
            ch = int(input("Enter you choice:"))
            if ch == 1:
                v = input("Enter a value:")
                listAppend(lst,v)
                display(lst)
            elif ch == 2:
                display(lst)
            elif ch == 3:
                r = input("Enter a value to remove:")
                lst = Remove(lst,r)
                print(f"List after removed {r} : {lst}")
            elif ch == 4:
                n = int(input("Enter the size of new list:"))
                l2 = [0] * n
                get(l2,n)
                print(Concat(lst,l2))
            elif ch == 5:
                display(lst)
                rep = int(input("Enter a number:"))
                print(repeat(lst,rep))
            elif ch == 6:
                display(lst)
                s = int(input("Enter a starting value:"))
                e = int(input("Enter a ending value:"))
                print(f"Sliced List: {Slice(lst,s,e)}")
            elif ch==7:
                display(lst)
                se = input("Enter a element to search:")
                print(Search(lst,se))
            elif ch == 8:
                break
            else:
                print("Invalide Choice")
    except ValueError as e:
            print(f"Error: {e}")
main()
