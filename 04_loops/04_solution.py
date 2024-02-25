# Problem: Reverse a string using a loop.

# get the string
input_string = "Python"
# variable to store reverse string
reverse_string = ""

# reverse the string using loop
for char in input_string:
    reverse_string = char + reverse_string
    # here what is happening
    # first reverse_string is ""(empty)
    # then we added => P + "" => "P"
    # then we added => y + "P" => "yP"
    # just by changing the position we can reverse the position

print(reverse_string)