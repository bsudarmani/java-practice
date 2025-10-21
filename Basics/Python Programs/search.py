import numpy as np
n = int(input("Enter number of elements:"))
a = np.zeros(n)
for i in range(0,n):
    s = "Enter num " + str(i+1) + ": "
    a[i] = int(input(s))

k = int(input("Enter a element to search:"))
def search(a,k):
    index=0
    for i in a:        
        if i == k:
            return [True,index]
        index= index + 1
    return [False,-1]

res = search(a,k)
if(res[0]):
    print("The Element ",str(k),"Found at the index ",str(res[1]),", at the position ",str(res[1]+1))
else:
    print("The Element ",str(k)," not found")
