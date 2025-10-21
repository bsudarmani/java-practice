def leap(n):
    if n <=0:
        raise ValueError("year can't be zero or negative number")
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return 1
        else:
            return 1
    return 0

def main():
    try:
        print("\tLEAP YEAR OR NOT")
        year = int(input("Enter a year: "))
        res = leap(year)
        if res == 1:
            print(f"The Given year {year} is a leap year")
        else:
            print(f"The Give year {year} is not a leap year")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        ch = input("Did you want to continue (Y/N): ")
        if ch == 'y' or ch == 'Y':
            main()

main()
