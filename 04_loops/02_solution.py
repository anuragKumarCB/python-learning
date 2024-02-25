# Problem: Calculate the sum of even numbers up to a given number n.

# get the n number
number_n = 10
# variable to store sum of even numbers
even_sum = 0

# check for each even number and add them to variable
for i in range(1, number_n+1):
    if i % 2 ==0:
        even_sum +=i

print(f"Sum of even numbers in given number {number_n} is :",even_sum)