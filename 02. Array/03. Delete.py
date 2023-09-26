import numpy as np

n = int(input("Enter the size of array: "))
array_ele = []

print("Enter", n, "elements: ")
for i in range(n):
    val = input(" ")
    array_ele.append(val)
arr = np.array(array_ele)
print("Initial array: \n",arr)

# Delete - Delete the element from the specified location
pos = int(input("Enter the position: "))
arr = np.delete(arr, pos)
print("Array after Deletion:\n",arr)
