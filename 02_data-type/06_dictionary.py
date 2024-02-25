# if we need to store multiple data then we have list but with list we can't
# define key value (index). So, for that we have dictionary where we can 
# definde both keys and values. key and value combined called an item.
# item order doesn't matter in dictionary unlike list.

chai_type = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Sour"}
print(chai_type)
# => {'Masala': 'Spicy'}    here - Mashala is Key and Spicy is Value

# access value using key
print(chai_type["Masala"])
# => Spicy  (accessing value is same as list instead of index we provide key)

# get() take key and give us back its value.
chai_type = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Grassy"}
chai_type.get("Masala")
# => 'Spicy'
chai_type.get("Green")
# => 'Grassy'

# difference between [key_name] way and get("key_name")
chai_type = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Grassy"}

# get()
chai_type.get("Masala")
# => 'Spicy'

# using [key_name]
chai_type["Ginger"]
# => 'Zesty'

# only difference is that when we proide wrong key then what it returns
# get()
chai_type.get("Masalaa")    # wrong key Masalaa not Masala
# => inside get() if key_name is wrong then it will return nothing

# using [key_name]
chai_type["Gingerr"]     # wrong key Gingerr not Ginger
# => it returns error below
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'Gingerr