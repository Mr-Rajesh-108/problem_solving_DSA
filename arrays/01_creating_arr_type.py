import array
# Create an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", int_array)


# Create an array of floats
float_array = array.array('f', [1.0, 2.0, 3.0, 4.0, 5.0])
print("Float Array:", float_array)

# Create an array of characters
# char_array = array.array('u', ['a', 'b', 'c', 'd', 'e']) # throw warning in python3.16 to remove 'u' typecode in future
# print("Character Array:", char_array)

# Create an array of doubles
double_array = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
print("Double Array:", double_array)

# Create an array of unsigned integers
uint_array = array.array('I', [1, 2, 3, 4, 5])
print("Unsigned Integer Array:", uint_array)

# Create an array of bytes
byte_array = array.array('b', [1, 2, 3, 4, 5])
print("Byte Array:", byte_array)

print("Array:", [elem for elem in byte_array])

x_times_2 = [elem * 2 for elem in byte_array]
print("Array with elements multiplied by 2:", x_times_2)


x_times_2.insert(2, 99)
print("Array after inserting 99 at index 2:", x_times_2)
x_times_2.remove(4) # removes first occurrence of 4 value

print("Array after removing first occurrence of 4:", x_times_2) 
deleted=[]

deleted.append(x_times_2.pop(2)) # removes element at index 3
print("Array after popping element at index 3:", x_times_2)
print("Popped element:", deleted)
deleted.append(x_times_2.pop()) # removes last element
print("Array after popping last element:", x_times_2)

print("Popped element:", deleted)

print('\n')
