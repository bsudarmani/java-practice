def Prime(n):
    if n <= 0:
        raise ValueError("number can't be negative")
    for i in range(2,int((n/2)+1)):
        if n % i ==0:
            return 0
    return 1

def main():
    try:
        print("\tPRIME NUMBER CHECKING")
        n = int(input("Enter a number: "))
        res = Prime(n)
        if res == 0:
            print(f"The Given number {n} is not a prime number")
        else:
            print(f"The Give number {n} is a prime number")
    except ValueError as e:
        print(e)
    finally:
        ch = input("Did you want to continue (Y/N): ")
        if ch=='y' or ch == 'Y':
            main()

main()
