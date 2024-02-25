# Problem: Write a function that takes variable number of arguments and returns their sum.

#  variable number of arguments using the *args syntax.
# The *args parameter allows you to pass any number of positional arguments
# to the function, and these arguments will be collected into a tuple.
def sum(*args):
    total = 0
    for num in args:
        total += num
    
    return total

print(sum(2, 4, 6, 8, 10))