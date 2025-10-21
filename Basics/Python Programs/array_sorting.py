import numpy as np
from numpy import where
def sort(arr,isDescending):
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    if isDescending:
        return arr[::-1]
    return  arr

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
            print("\tARRAY SORTING")
            a = getArray()
            a=sort(a,False)
            Display(a,"Ascending Order...")
            a=sort(a,True)
            Display(a,"Descending Order...")
            c = input("Did you want to continue (Y/N):")
            if c.lower() !='y':
                break
    except ValueError as e:
        print(f"Error = {e}")

Main()
