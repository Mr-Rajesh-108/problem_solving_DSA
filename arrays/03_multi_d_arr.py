import numpy as np

# Creating vector
vector = np.array([1, 2, 3.5, 4, 'a'])
print("Vector:", vector)

# Creating matrix vector
linespace_vector = np.linspace(10, 20, 11) # creates 11 evenly spaced numbers between 10 and 20
print("Linespace Vector:", linespace_vector)
matrix_vector = np.array(linespace_vector).reshape(11, 1) # reshaping to 11 rows and 1 column
print("Matrix Vector:\n", matrix_vector)

arrange_vector = np.arange(0, 21, 2) # creates numbers from 0 to 20 with a step of 2
print("Arrange Vector:", arrange_vector)

logspace_vector = np.logspace(1, 3, 5) # creates 5 numbers between 10^1 and 10^3
print("Logspace Vector:", logspace_vector)

arr = np.full((3, 4), 7) # creates a 3x4 matrix filled with 7s
print("Full Matrix:\n", arr)

# Creating special matrices
zeros_matrix = np.zeros((3, 4)) # 3 rows and 4 columns
print("Zeros Matrix:\n", zeros_matrix)
ones_matrix = np.ones((2, 5)) # 2 rows and 5 columns
print("Ones Matrix:\n", ones_matrix)
identity_matrix = np.eye(4) # 4x4 identity matrix
print("Identity Matrix:\n", identity_matrix)
random_matrix = np.random.rand(3, 3) # 3x3 matrix with
print("Random Matrix:\n", random_matrix)

# Basic operations
arr3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix:\n", arr3x3) 
print("Shape:", arr3x3.shape)
print("Data Type:", arr3x3.dtype)   
print("Transpose:\n", arr3x3.T)
print("Max:", arr3x3.max()) 
print("Min:", arr3x3.min())
print("Sum:", arr3x3.sum()) 
print("Mean:", arr3x3.mean())
print("Standard Deviation:", arr3x3.std())
print("Index of Max:", arr3x3.argmax())
print("Index of Min:", arr3x3.argmin())
print("Flattened Array:", arr3x3.flatten())
print("Reshaped Array (1x9):\n", arr3x3.reshape(1, 9))
print("Sliced Array:\n", arr3x3[0:2, 1:3])
print("Element at (2,2):", arr3x3[2, 2])
print("Elements greater than 5:", arr3x3[arr3x3 > 5])
print("Add 10:\n", arr3x3 + 10)
print("Multiply by 2:\n", arr3x3 * 2)
print("Matrix Multiplication:\n", np.dot(arr3x3, arr3x3))   
print("Element-wise Multiplication:\n", arr3x3 * arr3x3)
print("Square Root:\n", np.sqrt(arr3x3))
print("Exponentiation (e^x):\n", np.exp(arr3x3))
print("Logarithm:\n", np.log(arr3x3))
print("Sin:\n", np.sin(arr3x3))
print("Cos:\n", np.cos(arr3x3))
print("Tan:\n", np.tan(arr3x3))
# Saving and loading arrays
np.save('array.npy', arr3x3)
loaded_array = np.load('array.npy')
print("Loaded Array:\n", loaded_array)
