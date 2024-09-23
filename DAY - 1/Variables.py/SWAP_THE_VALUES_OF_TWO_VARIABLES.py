# SWAP THE VALUES OF TWO VARIABLES

# 5) Create two variables "x" and "y" with values "10" and "20". Swap their values without using a third variable. Print both variables after swapping.

#->
# Assign initial values to x and y
x = 10
y = 20

# Swap the values of x and y
x, y = y, x #Python allows easy swapping like this

# Print the swapped values
print("After swapping, x:",x) #output: 20
print("After swapping, y:",y) #output: 10