# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
# (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

import random
# define fruit color
fruit_color = ["Green", "Yellow", "Brown"]

# take the random color 
random_fruit_color  = random.choice(fruit_color)

if random_fruit_color == "Green":
    fruit_condition = "Unripe"

elif random_fruit_color == "Yellow":
    fruit_condition = "Ripe"

else:
    fruit_condition = "Overripe"

print(fruit_condition)