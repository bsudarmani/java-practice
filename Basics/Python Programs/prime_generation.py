def CheckPrime(n):
    
    for i in range (2,(n//2)+1,1):
        if n % i == 0:
            return False
    return True

def PrimeGeneration(n):
    if n<=0:
        raise ValueError("Number can't be zero or negative")
    a=[]    
    for i in range(2,(n*2)+1):
        if CheckPrime(i):
            a.append(i)
            
    return a

def main():
    while True:
        try:
            print("\tPRIME NUMBER GENERATION")
            n = int(input("Enter a number:"))
            print(f"First {n} Prime Numbers are:") 
            print(PrimeGeneration(n))        
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            ch = input("Did you want to continue (Y/N):")
            if ch.lower() != 'y':
                break
main()
