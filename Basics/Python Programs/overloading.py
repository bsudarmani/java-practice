from multipledispatch import dispatch
@dispatch(int)
def area(a):
    return f"Area of Square = {a * a}"
@dispatch(int,int)
def area(l,b):
    return f"Area of Rectangle = {l*b}"
@dispatch(float)
def area(r):
    return  f"Area of Circle = {3.14 * r * r}"
@dispatch(float,float)
def area(b,h):
    return f"Area of Triangle = {0.5 * b * h}"

def main():
    try:
        print("\tAREA OF SHAPES")
        lst = []
        print("Press 1 for square")
        print("Press 2 for circle")
        print("Press 3 for rectangle")
        print("Press 4 for Triangle")
        print("Press 5 for exit")
        while True:
            ch = int(input("Enter you choice:"))
            if ch == 1:
                v = int(input("Enter a number:"))
                print(area(v))
            elif ch == 2:
                v = float(input("Enter a number:"))
                print(area(v))
            elif ch == 3:
                l = int(input("Enter a length:"))
                b = int(input("Enter a breadth:"))
                print(area(l,b))
            elif ch == 4:
                b = float(input("Enter a length:"))
                h = float(input("Enter a breadth:"))
                print(area(b,h))
            elif ch == 5:
                break
            else:
                print("Invalide Choice")
    except ValueError as e:
            print(f"Error: {e}")
main()
