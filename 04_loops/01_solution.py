# Problem: Given a list of numbers, count how many are positive.

# get the number
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# make a variable that will count positive numbers
positive_number_count = 0

# check for each number in given number
for num in numbers:
    if num > 0:
        positive_number_count += 1

print("Positive numbers in given number are :", positive_number_count)