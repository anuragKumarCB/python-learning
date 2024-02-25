# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# get a number
number = 3

# print the multiplication table for the given number
for i in range(1, 11):
    if i == 5:
        continue
    print(number, "x", i, "=", number*i)

    # if i == 5:
    #     pass     # This line does nothing, effectively skipping it
    # else:
    #     print(number, "x", i, "=", number*i)