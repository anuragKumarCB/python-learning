# Problem: Write a function multiply that multiplies two numbers,
# but can also accept and multiply strings.

# we can multiply string if one is string and one is integer
def multiply(value1, value2):
    
    result = value1 * value2
    return result

print(multiply("OddOne", 5))