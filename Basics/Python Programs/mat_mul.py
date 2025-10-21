import numpy as np

#matrix multiplication
def getMatrix(r,c):
    mat = np.zeros((r,c),dtype=int)
    for i in range(r):
        for j in range(c):
            mat[i,j] = int(input(""))
    return mat

def putMatrix(mat,r,c):
    for i in range(r):
        for j in range(c):
            print(f"{mat[i,j]}",end="  ")
        print()

def operation(m1,m2,r1,c1,r2,c2):
    mat = np.zeros((r1,c2),dtype=int)
    print("Matrix Multiplication:")
    for i in range(r1):
        for j in range(c2):
            mat[i][j] = 0
            for k in range(r2):
                mat[i,j] += m1[i,k] * m2[k,j]
    return mat
#logic
while True:
    try:
        print("\tMATRIX MULTIPLICATION")
        print("Enter Matrix 1 Row X Column:")
        r1 = int(input("Enter a no. of rows:"))
        c1 = int(input("Enter a no. of columns:"))
        print(f"Enter Matrix 1 {r1}X{c1}:")
        m1 = getMatrix(r1,c1)
        print("Enter Matrix 2 Row X Column:")
        r2 = int(input("Enter a no. of rows:"))
        c2 = int(input("Enter a no. of columns:"))
        print(f"Enter Matrix 2 {r2}X{c2}:")
        m2 = getMatrix(r2,c2)
        print(f"Matrix 1 {r1}X{c1}:")
        putMatrix(m1,r1,c1)
        print(f"Matrix 2 {r2}X{c2}:")
        putMatrix(m2,r2,c2)
        if c1 == r2:
            res = operation(m1,m2,r1,c1,r2,c2)
            putMatrix(res,r1,c2)
        else:
            raise ValueError("Matrix multiplication can't be performed")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        ch = input("Did you want to continue(Y/N):")
        if ch.lower() != 'y':
            print("Thank You")
            break
