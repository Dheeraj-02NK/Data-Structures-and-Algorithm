import numpy as np

n = int(input("Enter the size of array: "))
array_ele = []

print("Enter", n, "elements: ")
for i in range(n):
    val = input(" ")
    array_ele.append(val)
arr = np.array(array_ele)
print("Initial array: \n",arr)

# append - adds the element to the last position
# np.append(array, element)
new = input("Enter the element to append: ")
arr = np.append(arr, new)
print("Array after appending:\n",arr)

# insert -  adds the element to the specified position
# np.insert(array, index, element
new = input("Enter the element to insert: ")
pos = int(input("Enter the position: "))
arr = np.insert(arr, pos, new)
print("array after insertion:\n", arr)