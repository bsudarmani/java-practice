def sumDigit(a):
    if a<=0:
        raise ValueError("Number can't be zero or negative")
    res = 0
    while a!=0:
        rem = a % 10
        res += rem
        a//=10
    if res > 9:
        return sumDigit(res)
    else:
        return res

def main():
    while True:
        try:
            print("\tSUM OF DIGITS")
            m = int(input("Enter a number:"))
            print(f"Sum of digit {m} = {sumDigit(m)}")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            ch = input("Did you want to continue(Y/N): ")
            if ch.lower() != 'y':
                break
main()
