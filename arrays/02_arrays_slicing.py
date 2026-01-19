from array import *

# Slicing........
arrayInt= array('i', [10,20,30,40,50,60,70,80,90])
print("Original Array:", [x for x in arrayInt])

sliced_array = arrayInt[2:7]  # Slicing from index 2 to 6
print("Sliced Array (index 2 to 6):", [x for x in sliced_array])

print('\n')
reversedArr = arrayInt[::-1]  # Reversing the array using slicing
print("Reversed Array:", [x for x in reversedArr])


# insert elements in empty array using slicing
emptyArray = array('i', []) 
emptyArray[0:0] = array('i', [1, 2, 3, 4, 5])  # Inserting elements at the start
print("Array after inserting elements using slicing:", [x for x in emptyArray])
print('\n')
# Modify elements using slicing
arrayInt[1:4] = array('i', [25, 35, 45])  # Modifying elements from index 1 to 3
print("Array after modifying elements using slicing:", [x for x in arrayInt])
print('\n')
# Delete elements using slicing
arrayInt[3:5] = array('i', [])  # Deleting elements from index 3 to 4
print("Array after deleting elements using slicing:", [x for x in arrayInt])


# insert elements in empty array using user input
userArray = array('i', []) 
n = int(input("Enter number of elements to insert in array: "))
try:
    if n < 0:
        raise ValueError("Number of elements cannot be negative.")
    else:
        for i in range(n):
            element = int(input(f"Enter element {i+1}: "))
            try:
                userArray[i:i] = array('i', [element])  # Inserting element at index i using slicing
            except IndexError:
                print("Index out of bounds.")
        print("User Array after inserting elements using slicing:", [x for x in userArray])
except ValueError as ve:
    print(ve)

print('\n')

