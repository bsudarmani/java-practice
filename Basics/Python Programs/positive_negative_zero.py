def PZN(n):
    if n == 0:
        return f"The Given number is a zero")
    else if n > 0 :
        return f"The Given number {n} is a positive number"
    else:
        return f"The Given number {n} is a negative number"

def main():
    print("\tPOSITIVE , NEGATIVE OR ZERO")
    n = int(input("Enter a number: "))
    print(PZN(n))
    ch = input("Did you want to continue (Y/N): ")
    if ch == 'y' or ch == 'Y':
        main()
main()
