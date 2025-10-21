
 #matrix transpose
import numpy as np
def getMatrix(r,c):
    mat = np.zeros((r,c),dtype=int)
    for i in range(r):
        for j in range(c):
            mat[i,j] = int(input(""))
    return mat

def putMatrix(mat,r,c,isTranspose):
    for i in range(r):
        for j in range(c):
            if isTranspose:
                print(f"{mat[j,i]}",end="  ")
            else:
                print(f"{mat[i,j]}",end="  ")
        print()

#logic
while True:
    try:
        print("\tMATRIX TRANSPOSE")
        r = int(input("Enter a no. of rows:"))
        c = int(input("Enter a no. of columns:"))
        if r!=c:
            raise ValueError("Row and column must be same")
        print(f"Enter Matrix {r}X{c}:")
        m = getMatrix(r,c)
        print(f"Matrix {r}X{c}:")
        putMatrix(m,r,c,False)
        print("Transpose:")
        putMatrix(m,r,c,True)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        ch = input("Did you want to continue(Y/N):")
        if ch.lower() != 'y':
            print("Thank You")
            break
