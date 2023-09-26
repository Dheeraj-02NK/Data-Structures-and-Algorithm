import numpy as np

n = int(input("Enter the size of array: "))
array_ele = []

print("Enter", n, "elements: ")
for i in range(n):
    val = input(" ")
    array_ele.append(val)

arr = np.array(array_ele)

print(arr)