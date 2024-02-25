# Problem: Create a lambda function to compute the cube of a number.

# lambda is a keyword used to create small anonymous functions. An 
# anonymous function is a function defined without a name. Lambda functions
# are useful when you need a simple function for a short period of time or
# when you want to pass a function as an argument to another function.

cube = lambda number: number ** 3

print(cube(5))