class Fibo:
    def __init__(self,u):
        m,n = 1,-1
        for i in range(u):
            c = m + n
            print(c)
            m,n = c,m
print("\tFIBONACII SERIES")
f = Fibo(int(input("Enter a N number to generate: ")))
