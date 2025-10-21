def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

def main():
    while True:
        print("\tFACTORIAL OF A NUMBER")
        n = int(input("Enter a number: "))
        print(f"Factorial of {n} = {fact(n)}")
        ch = input("Did you want to continue(Y/N):")
        if ch.lower() !='y':
            break
main()
