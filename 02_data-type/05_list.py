# List or array (in other languages) starts with 0 index base.
# So we can give the index value and take the element out.
tea_varieties = ["Red", "Green", "White", "Oolong"]
print(tea_varieties[0])
# => Red 
print(tea_varieties[3])
# => Oolong
print(tea_varieties[-1])
# => Oolong (negative index will start at the end)


# List and String both are treated like each other but they are not the same.
# we can use two range value inside slice [ 1st : 2nd ]. First value is starting index and last
# value is ending index but last value is always excluded meaning last index will not be included.
tea_varieties = ["Red", "Green", "White", "Oolong"]

# [ : ]  slice the full list
print(tea_varieties[:])
# => ['Red', 'Green', 'White', 'Oolong']

# [ 1st : ] start with first index and go to last index
print(tea_varieties[2:])
# => ['White', 'Oolong']

# [  : 2nd ] start with 0 index and go to second index
print(tea_varieties[:2])
# => ['Red', 'Green']

# [ 1st : 2nd ] start with first index and go to second index
print(tea_varieties[0:3])
# => ['Red', 'Green', 'White']

# there are two way to reassign elements using index value.

# directly providing index value and assigning the element.
tea_varieties = ["Red", "Green", "White", "Oolong"]
print(tea_varieties[2])
# => White
tea_varieties[2] = "Lemon"
print(tea_varieties)
# => ['Red', 'Green', 'Lemon', 'Oolong']

# we can use slice to reassign elements but we use slice then it expects 
# list/array so we have to provide element value using an list/array.
print(tea_varieties[1:2])
# => ['Green']
tea_varieties[1:2] = ["Herbal"]
print(tea_varieties)
# => ['Red', 'Herbal', 'Lemon', 'Oolong']

# if we dont provide element value using list/array then this happens
tea_varieties[1:2] = "Herbal"
print(tea_varieties)
# => ['Red', 'H', 'e', 'r', 'b', 'a', 'l', 'Lemon', 'Oolong']
# so we have to use list/array to provide element value.

# benefit of using slice is that we can reassign multiple element values at a time
tea_varieties = ["Red", "Green", "White", "Oolong"]
print(tea_varieties)
# => ['Red', 'Green', 'White', 'Oolong']
tea_varieties[1:3] = ["Herbal", "Ginger"]
print(tea_varieties)
# => ['Red', 'Herbal', 'Ginger', 'Oolong']


# Well first of all we shouldn’t do that. But lets see -

tea_varieties = ["Red", "Green", "White", "Oolong"]
print(tea_varieties[1:1])
# => []
# it retruns us an empty list because we are starting at 1 index and ending at 1 index but
# as we know last index value is excluded so its empty list.

# what happen is we add somthing using [1:1]
tea_varieties[1:1] = ["chai", "another-chai"]
print(tea_varieties)
# => ['Red', 'chai', 'another-chai', 'Herbal', 'Ginger', 'Oolong']
# it went to 1 index but didn't replaced anything because it stated at 1 and ended at 1 but
# becuase end index is excluded so it shifted all the emelents and added the elements

# we can remove elements by using [] (empty list) too
tea_varieties[1:3] = []
print(tea_varieties)
# => ['Red', 'Herbal', 'Ginger', 'Oolong']
# we went index 1 and 2 (last index excluded) and added an empty list or nothing

# to use for loop we just need to do - for variable_name in list_name
tea_varieties = ["Red", "Green", "White", "Oolong"]
for each_tea in tea_varieties:
	print(each_tea)
# => Red
# => Green
# => White
# => Oolong
	
# here we get another variable in print statement - end.
# end give us what we want to end with. by default its \n
for each_tea in tea_varieties:
	print(each_tea, end="-")
# => Red-Green-White-Oolong-    (here we added dash so we got dash after each element)

# append() method let us add elements at the end of list.
tea_varieties = ["Black-Tea", "Green-Tea", "White-Tea", "Herbal-Tea"]
print(tea_varieties)
# => ['Black-Tea', 'Green-Tea', 'White-Tea', 'Herbal-Tea']
tea_varieties.append("Oolong-Tea")
print(tea_varieties)
# => ['Black-Tea', 'Green-Tea', 'White-Tea', 'Herbal-Tea', 'Oolong-Tea', 'Oolong-Tea']

# pop method removes the last element without manual looping.
# it doesn't need any parameter.
tea_varieties = ['Black-Tea', 'Green-Tea', 'White-Tea', 'Herbal-Tea', 'Oolong-Tea']
print(tea_varieties)
# => ['Black-Tea', 'Green-Tea', 'White-Tea', 'Herbal-Tea', 'Oolong-Tea', 'Oolong-Tea']
tea_varieties.pop()
# => 'Oolong-Tea'
print(tea_varieties)
# => ['Black-Tea', 'Green-Tea', 'White-Tea', 'Herbal-Tea']

# remove() give us ability to remove element by using element (value).
tea_varieties = ['Black-Tea', 'Green-Tea', 'White-Tea', 'Herbal-Tea', 'Oolong-Tea']
print(tea_varieties)
# => ['Black-Tea', 'Green-Tea', 'White-Tea', 'Herbal-Tea', 'Oolong-Tea']
tea_varieties.remove("White-Tea")
print(tea_varieties)
# => ['Black-Tea', 'Green-Tea', 'Herbal-Tea', 'Oolong-Tea']

# insert() lets us add element with index position.
# insert() take two parameter  -first is index value, second is element
tea_varieties = ['Black-Tea', 'Green-Tea', 'Herbal-Tea', 'Oolong-Tea']
print(tea_varieties)
# => ['Black-Tea', 'Green-Tea', 'Herbal-Tea', 'Oolong-Tea']
tea_varieties.insert(2, "White-Tea")
print(tea_varieties)
# => ['Black-Tea', 'Green-Tea', 'White-Tea', 'Herbal-Tea', 'Oolong-Tea']

# copy() let us copy the entire list (not same reference).
tea_varieties = ['Black-Tea', 'Green-Tea', 'Herbal-Tea', 'Oolong-Tea']

# we can copy entire list three ways-

# copy using = 
tea_varieties_copy_reference = tea_varieties
# this will copy the list but both have same reference so its
# more like assigining the same reference to two variables

# we can copy using slice too but that's not best practice.
tea_varieties_copy_slice = tea_varieties[:]
# now we have copy of list and both have different reference.

# using copy()
tea_varieties_copy = tea_varieties.copy()
print(tea_varieties_copy)
# => ['Black-Tea', 'Green-Tea', 'Herbal-Tea', 'Oolong-Tea']
# now we have copy of the list but its more of a cleaner way

# range take an argument and based on that argument value it will
# provide us with a range from 0 to that argument value -1
# (because in Python last value is not included).

# range(10) range of 0 to 9
print(range(10))
# => range(0, 10) it show 0-10 but last value is excluded
print(range(100))
# => range(0, 100) same here 0-99, 100 is excluded

# sometime we generate element/value inside an empty list, that is list comprehension.

# for example generating squared number in given range (number * number)
squared_num = [x**2 for x in range(10)]
# here x is variable, and for square we need to do - x**2 means - x * x
# after that we have for loop for x in range between 0-9 (last value excluded)
print(squared_num)
# => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# for example generating cube number in given range (number * number * number)
cube_num = [y**3 for y in range(10)]
# here y is variable, and for cube we need to do - y**3 means - y * y * y
# after that we have for loop for y in range between 0-9 (last value excluded)
print(cube_num)
# => [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]