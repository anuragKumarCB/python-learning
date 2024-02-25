# Problem: Create a function that accepts any number of keyword
# arguments and prints them in the format key: value.

# You can use **kwargs in Python to accept any number of keyword arguments,
# and then iterate over them to print each key-value pair
def key_value_pair(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

key_value_pair(key1="value1", key2="value2", key3="value3")