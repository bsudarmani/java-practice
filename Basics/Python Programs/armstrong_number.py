#Armstrong number checking
def armstrong_checker(n): #function to find armstrong number or not
    if n <=0:
        raise ValueError("Value can't be zero or negative")
    temp = n
    res = 0
    digit = len(str(n)) #number is converted to string to find its digit
    while n!=0:
        rem = n % 10;
        res = res + ( rem ** digit ) # ** operator used to do power but also a function can also be used or created
        n //= 10 
    return temp == res

def main():
    while True:
        try:
            print("\tARMSTRONG NUMBER CHECKING")
            a = int(input("Enter a number:"))
            res = armstrong_checker(a)
            if res:
                print(f"The Given number {a} is a armstrong number")
            else:
                print(f"The Given number {a} is not a armstrong number")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            ch = input("Did you want to continue (Y/N): ")
            if ch.lower() !='y':
                break
main()
