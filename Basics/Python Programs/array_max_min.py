import numpy as np
def min_max(arr):
    n = len(arr)
    minimum = arr[0]
    maximum = arr[0]
    for i in range(n):
        if arr[i] < minimum:
            minimum = arr[i]
        if arr[i] > maximum:
            maximum = arr[i]
    return minimum,maximum

def Display(arr,text):
    print(text)
    for i in arr:
        print(i,end='  ')
    print()
def getArray():
    n = int(input("Enter number of elements:"))
    arr = np.array([],int)
    for i in range(n):
        arr = np.append(arr,int(input(f"Enter Num {i+1}:")))
    return arr
def Main():
    try:
        while True:
            print("\tARRAY MIN & MAX")
            a = getArray()
            res = min_max(a)
            Display(a,"Elements are...")
            print(f"Min = {res[0]}\nMax = {res[1]}")
            c = input("Did you want to continue (Y/N):")
            if c.lower() !='y':
                break
    except ValueError as e:
        print(f"Error = {e}")

Main()
