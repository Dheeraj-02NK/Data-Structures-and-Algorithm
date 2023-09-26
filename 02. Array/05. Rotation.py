import numpy as np

# Get the dimensions of the 2D array from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matx =rows*cols
# Initialize an empty list to store the user input
lst = []

# Loop to take user input for each element
print("Enter", matx, "elements: ")
for i in range(rows):
    row_input = []
    for j in range(cols):
        element = float(input(""))
        row_input.append(element)
    lst.append(row_input)

# Convert the list to a NumPy array
array_2d = np.array(lst)

# Print the resulting 2D NumPy array
print("Initial 2D Array:\n", array_2d)

# Rotation
rotated_array = np.rot90(array_2d,k=1)
print("Rotated array:\n", rotated_array)
