import numpy as np

# evenly spaced array 

array = np.arange(9)
print(array)

# add a 2nd arguement start = 5, stop = 15, again no step added

array1 = np.arange(5, 15)
print(array1) # still  has step size of 1

# 3rd arguement to add step

array2 = np.arange(0, 15, 2)
print(array2)

# can pass decimals - use nplinspace for decimal arrays though

array3 = np.arange(0, 15, .5)
print(array3)

#using linspace to print floats.
array4 = np.linspace(0.5, 10.5)


