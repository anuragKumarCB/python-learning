# Problem: Given a string, find the first non-repeated character.

# get the string
input_string = "teeteracdacd"

# check for first noo-repeated char (then stop the loop)
for char in input_string:
    if input_string.count(char) == 1:
        print("First non-repeated character is -", char)
        break   # breaking loop because we just needed firs non-repeated char
