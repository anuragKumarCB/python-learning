# Problem: Check if all elements in a list are unique.
# If a duplicate is found, exit the loop and print the duplicate.

# get the list
items = ["apple", "banana", "orange", "banana", "mango"]

for element in items:
    if items.count(element) > 1:
        print("Duplicate:", element)
        break

# sir's way of doing things

# unique_item = set()

# for elment in items:
#     if element in unique_item:
#         print("Duplicate:", element)
#         break
#     unique_item.add(element)