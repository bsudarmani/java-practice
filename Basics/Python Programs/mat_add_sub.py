import numpy as np

#matrix addition and subtraction
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

def operation(m1,m2,op,r,c):
    mat = np.zeros((r,c),dtype=int)
    if op == '+':
        print("Matrix Addition:")
        for i in range(r):
            for j in range(c):
                mat[i,j] = m1[i,j] + m2[i,j]
        return mat
    elif    op == '-':
        print("Matrix Subtraction:")
        for i in range(r):
            for j in range(c):
                mat[i,j] = m1[i,j] - m2[i,j]
        return mat
    else:
        raise ValueError("Invalid Operator")

#logic
while True:
    try:
        print("\tMATRIX ADDITION OR SUBTRACTION")
        r = int(input("Enter a no. of rows:"))
        c = int(input("Enter a no. of columns:"))
        print(f"Enter Matrix 1 {r}X{c}:")
        m1 = getMatrix(r,c)
        print(f"Enter Matrix 2 {r}X{c}:")
        m2 = getMatrix(r,c)
        print(f"Matrix 1 {r}X{c}:")
        putMatrix(m1,r,c)
        print(f"Matrix 2 {r}X{c}:")
        putMatrix(m2,r,c)
        op = input("Enter the operator(-,+): ")
        res = operation(m1,m2,op,r,c)
        putMatrix(res,r,c)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        ch = input("Did you want to continue(Y/N):")
        if ch.lower() != 'y':
            print("Thank You")
            break
