def rev(a):
    r = ''
    for i in range(len(a)-1,-1,-1):
        r+=a[i]
    return r

def main():
    while True:
        try:
            print("\tPALINDROME CHECKING")
            print("\t---------- --------")
            n = input("Enter a string:")
            t = n.lower()
            r = rev(t)
            if t == r:
                print(f"The Given value {n} is a palindrome")
            else:
                print(f"The Given value {n} is not a palindrome")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            ch = input("Did you want to continue (Y/N): ")
            if ch.lower() !='y':
                break
main()
    
    
