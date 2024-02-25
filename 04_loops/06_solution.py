# Problem: Compute the factorial of a number using a while loop.

# get a number
input_number = 8
input_num = input_number
factorial = 1

while input_number > 0:     # while lopp workd when condition is true
    factorial = factorial * input_number
    input_number = input_number - 1

print(f"Factorial of {input_num} is -",factorial)