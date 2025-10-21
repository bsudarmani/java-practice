import numpy as np


arr1 = list(map(int, input("Enter first array elements (comma separated): ").split(',')))
arr2 = list(map(int, input("Enter second array elements (comma separated): ").split(',')))


array1 = np.array(arr1)
array2 = np.array(arr2)


print("\n--- Element-wise Comparisons ---")
print("array1 == array2 :", array1 == array2)
print("array1 != array2 :", array1 != array2)
print("array1 <  array2 :", array1 < array2)
print("array1 <= array2 :", array1 <= array2)
print("array1 >  array2 :", array1 > array2)
print("array1 >= array2 :", array1 >= array2)


print("\n--- any() and all() ---")
print("Any elements equal?:", np.any(array1 == array2))
print("All elements equal?:", np.all(array1 == array2))

print("\n--- Using where() ---")
equal_indices = np.where(array1 == array2)
not_equal_indices = np.where(array1 != array2)

print("Indices where elements are equal:", equal_indices[0])
print("Indices where elements differ:", not_equal_indices[0])


print("\n--- Using nonzero() ---")

nonzero_indices_arr1 = np.nonzero(array1)
nonzero_indices_arr2 = np.nonzero(array2)

print("Non-zero indices in array1:", nonzero_indices_arr1[0])
print("Non-zero indices in array2:", nonzero_indices_arr2[0])


print("\n--- Differences explicitly ---")
for i in range(min(len(array1), len(array2))):
    print(f"Index {i}: array1={array1[i]} array2={array2[i]}")
