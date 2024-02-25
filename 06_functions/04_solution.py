# Problem: Create a function that returns both the area and circumference of a circle given its radius.

# Area=πr**2
# Circumference=2πr

import math
def area_and_circumference(radius):
    area = print(f"Area of {radius} is :", round(math.pi * (radius ** 2), 2))
    circumference = print(f"Circumference of {radius} is :", round(2 * (math.pi * radius)))

    return area, circumference

area_and_circumference(13)

# round(variable, 2)    lets us round the decimal value in given variable by a specific number
# here we are rounding varable value to 2 decimal points