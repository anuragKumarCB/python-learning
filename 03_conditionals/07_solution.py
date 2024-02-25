# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

import random
# define order size and extra shot of espresso
order_size = ["Small", "Medium", "Large"]
random_order_size = str(random.choice(order_size))

espresso = False

if espresso:
    coffee = random_order_size + " coffee with an extra shot"

else:
    coffee = random_order_size + " coffee"

print(coffee)