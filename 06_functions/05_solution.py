# Problem: Write a function that greets a user.
# If no name is provided, it should greet with a default name.

def greet_user(name):
    default_name = "User"
    if name: print(f"Hello {name}")
    else: print(f"Hello {default_name}")
    return

greet_user("")