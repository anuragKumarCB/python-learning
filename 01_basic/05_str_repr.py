# In Python, the str() and repr() functions are used to obtain string representations of objects.
# While they may seem similar at first glance, there are some differences in how they behave.
# Both of the functions can be helpful in debugging or printing useful information about the object.

# Python str()
# Python str() function is used to convert an object to its string representation.It is a built-in
# function that can be used to convert objects of different data types, such as integers, and floats.
s = 'Hello, Geeks.'
print (str(s))
print (str(2.0/11.0))
# -> Hello, Geeks.
# -> 0.181818181818

# Python repr()
# Python repr() Function returns a printable representation of an object in Python. In other words,we can say that
# the Python repr() function returns a printable representation of the object by converting that object to a string.
s = 'Hello, Geeks.'
print (repr(s))
print (repr(2.0/11.0))
# -> 'Hello, Geeks.'
# -> 0.18181818181818182