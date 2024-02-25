# We get string in 3 varieties in Python. First is – single quotes,
# second is – double quotes, and third is – triple quotes.

# in all quotes – single, double, and tripe formatting is safe.
# Means if you add tab in string it will reflect in print statement.
# The only difference is that if you try to go to next line in 
# single quotes and double quotes it will not work but in triple quotes
# it will work and will also reflect in print statement.Tab will reflect
# directly by tab space but new line will reflect with \n.

# single quotes -
chai = 'mashal chai'
# => 'mashal chai'

# double quotes -
chai = "mashal      chai"
# => 'mashal      chai'

# triple quotes -
chai = """mashal
        chai"""
# => 'mashal\n        chai'


chai = 'Mashala chai'

# String is Treated as List so we can directly get the value by doing [ index_value ].
first_char = chai[0]
# => M

# we can use two range value to slice inside [ 1st : 2nd ]. First value is starting index and
# last value is ending index but last value is always excluded meaning it will not be included.
slice_chai = chai[0:7]
# => 'Mashala'

# you can do negative indexing. -1 index value will start from the last char in the string.
# But why complicate it when you can do it with a positive index?
slice_chai = chai [-1:]
# => 'i'

num_list = '0123456789'

# [:] empty index value will copy the all index.
num_list[ : ]
# => '0123456789'

# [1st : ] only first index value will start from that index and go to the end index.
num_list[ 3 : ]
# => '3456789'

# [ : 2nd ] only second value will start from first index and go to last index but exclude it.
num_list[ : 7]
# => '0123456'

# [ 1st : 2nd : 3rd ] if we provide 3 value last value is hoping (jump) value meaning
# how many char to jump each time.
num_list[ 0 : 7 : 2]	# jump by 2 each-time
# => '0246'
num_list[ 0 : 7 : 3 ]	# jump by 3 each-time
# => '036'



# lower() will convert string to lower case.
chai = 'Masala Chai'
print(chai.lower())
# => masala chai

print(chai) 
# => Masala Chai   (but chai same because of immutability.)

# upper() will convert string to upper case.
chai = 'Masala Chai'
print(chai.upper())
# => MASALA CHAI

print(chai) 
# => Masala Chai   (but chai same because of immutability.)

# strip() will remove extra white-spaces before and after the string.
chai = '		Mashala Chai		'
print(chai.strip())
# => Masala Chai

# replace() takes two value – first which one to replace and second which one to replace with.
chai = 'Lemon Chai'
print(chai.replace('Lemon', 'Ginger'))
# => Ginger Chai

# split() will split the string and returns you a new list.
# split() takes value to split them based on. Here is example based on
# comma and space (', '). default value of split() is space (based on space).
chai = 'Ginger, Lemon, Mint, Masala'
print(chai.split(', '))
# => ['Ginger', 'Lemon', 'Mint', 'Masala']

# find() will take a value/string/char and give back starting index of that
# value in that string. If you get -1 then that means that value/string/char
# does not exist in that given string.
chai = 'Masala Chai'
print(chai.find('Chai'))
# => 7

# count() will take a value/string/char and give back how many time that
# value/string/char is present in the given string. 0 means it doesn't exist.
chai = "Masala Chai Chai Chai"
print(chai.count('Chai'))
# => 3

# format() is used to inject variables in a string that have placeholder ( { } ) in it.
# order of variables is based on variables being injected in format().
chai_type = 'Masala'
quantity = 2
order = 'I ordered {} cups of {} chai'
print(order)
# => I ordered {} cups of {} chai
print(order.format(quantity, chai_type))
# => I ordered 2 cups of Masala chai

# "".join will change the list into string based on values given in "" (double-quotes).
# "".join() without any value
chai_variety = ['Ginger', 'Lemon', 'Mashala', 'Mint', 'Red']
print("".join(chai_variety))
# => GingerLemonMashalaMintRed

# " ".join() with space
print(" ".join(chai_variety))
# => Ginger Lemon Mashala Mint Red

# "-".join() with dash
print("-".join(chai_variety))
# => Ginger Lemon Mashala Mint Red

# ", ".join() with comma and then space
print(", ".join(chai_variety))
# => Ginger, Lemon, Mashala, Mint, Red

# len() is to get the total length of string including spaces.
chai = "Masala Chai"
print(len(chai))
# => 11

# for letter - for loop for string. here letter represents char in string.
# you can change letter with any word of your choice.
# here \n is automatically inject after each letters.
chai = "Masala Chai"
for letter in chai:
    print(letter)
# for char in chai:
#     print(char)

# => M
# => a
# => s
# => a
# => l
# => a

# => C
# => h
# => a
# => i
    
# when you have to use double-quotes inside double-quotes,
# how will python understand which is which in that case python
# will just print the string between the first two double-quotes and
# leave the rest. In that case we can do that we use single-quotes
# outside and then double-quotes inside. But there is another method
# called escaping the char by using \.
chai = "He said, "Masala chai is awesome""
print(chai)
# =>File "<stdin>", line 1
#     chai = "He said, "Masala chai is awesome""
#                       ^^^^^^
# SyntaxError: invalid syntax

# use single-quotes outside and double-quotes inside
chai = 'He said, "Masala chai is awesome"'
print(chai)
# => He said, "Masala chai is awesome"

# better way of doing it by escaping (\) the character 
chai = "He said, \"Masala chai is awesome\""
print(chai)
# => He said, "Masala chai is awesome"

# when we are working with path for windows path then we get problem of \ many times.
# We can fix it by escaping the character or by using r(raw) string (better method).

# if we do it normally then we get an error
path = "c:\user\pwd"
print(path)
#  File "<stdin>", line 1
#     path = "c:\user\pwd"
#                         ^
# SyntaxError: (unicode error) 'unicodeescape' codec can't
# decode bytes in position 2-3: truncated \uXXXX escape

# if we do it by escaping the character 
path = "c:\\user\\pwd"
print(path)
# => c:\user\pwd    (but problem here is lots of \ and we can get confused too)

# so we use r(raw) string
path = r"c:\user\pwd"
print(path)
# => c:\user\pwd

# we can ask python if a string contains the element we are providing.
# we can do that by giving the element then in and then variable.

chai = "Masala Chai"
print("Masala" in chai)	# here chai is variable
# => True

print("Lemon" in chai)	# here chai is variable
# => False