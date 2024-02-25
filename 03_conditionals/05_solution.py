# Problem: Suggest an activity based on the weather (e.g., Sunny -
# Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

import random
# define weather list
weather_today = ["Sunny", "Rainy", "Snowy"]

# get random weather
random_weather = random.choice(weather_today)

if random_weather == "Sunny":
    activity = "Go fo walk."

elif random_weather == "Rainy":
    activity = "Read a book"

elif random_weather == "Snowy":
    activity = "Buid a snowman"

print(activity)