# Mathematical / Arithmetical operators in Python -
# Addition -
234 + 345
# Subtraction -
289 - 234
# Multiplication -
324 * 245
# Division -
3546 / 34
# Power -
2 ** 1000
# Modules -
67 % 7

# mathematical-operations
# Bad practice – 

2 + 3 -4 * 5 / 6
# If you have to use all the mathematical operators use parentheses ( ).
# We all know that any operator parentheses get resolved first so why not use it.

# Good practice –

2 + ( 3  - 4 ) * ( ( 5 / 6 ) )
# If we add prenthese then is will get resolved first, but it we more than two operations going on.
# Then  use double prenthese it will get resolved first then single prenthese then operation without prenthese.


# precision 
# bad practice -

40 + 2.23
# python will automatically go for higher precession but codes should
# specifically decide for which precession they want to go for.

# good practice -

float(40) + 2.23
40 + int(2.23)
# this way you are specifically telling the program which precession you wants to go for and also,
# we have these methods available for use to make it more precise then why not use it.

# When we use two-three variables separating then by comma ( , ),
# they will give back Tuple –
x = 2
y = 3
z = 4

x,y,z
#  -> (2, 3, 4)     because we are using comma ( , ) they are return as tuple

x + 1, y * 3
#  -> (3, 9)        both operations are seperate but by using comma we did ien one line

# Boolens are treated as Number in Python
2 < 3
# => True
True == 1
# => True
True == 0
#  => False
False == 0
# => True
False == 1
# => Flase

# In python perspective Booleans are Number but we just add wrapper of true-false for our convenience

# We can use math library in Python and get so many useful methods for numbers. Example –

import math
# math.floor( ) –
# math.floor( ) will always result in down-line of number chain.

math.floor( 3.9 )
# => 3	(down-line of number chain is 3)
math.floor( -3.2 )
# => -4	(down-line of number chain -4)

# math.trunc( ) –
# mat.trunc( ) will always result in closest to zero

math.trunc( 2.9 )
# => 2	(closest to zero is 2)
math.trunc( -5.9 )
# => -5	(closest to zero is -5) 

# Python provides us with imaginary number to work with too.
# We can use these number in scientific or mathematical problem solving.
(2 + 1j) * 3
# => (6 + 3j)

# Python provide us with octal-literal number that is based to the 8.
# To use octal number we need to start the number with 0o (zero and then o)
# and it will give us value for that octal number.
0o20
# => 16
# We can use oct() method to get the octal-value of give number/data.
oct(62)
# => '0o76'

# Python provides us with Hex-number.
# To use hex number we need to start the number with 0x (zero and then x)
# and it will give us value for that hex number.
0xFF
# => 255
# We can use hex() method to get the hex-value of give number/data.
hex(68)
# => '0x44'

# Python provides us with binary numbers.
# To use binary numbers we need to start the number with 0b (zero and then b)
# and it will give us value for that binary number.
0b1000
# => 8
0b1010101011
# => 683
# We can use bin() method to get the bin-value of give number/data.
bin(95)
# => '0b1011111'

# For octal, hex, binary they have their own methods – oct(), hex(), and bin()
# to get the value of given number/data. But we can use int() method to get the
# same values as those methods. For that inside int() method we need to pass two
# thing –first is number/data wrapped in quotes, second is which base you want to
# use to convert the number/data (8 is octal, 16-base, 2 is binary).
int('62', 8)	# octal
# => 50
int('68', 16)	# 16-base
# => 104
int('1010101011', 2)	# binary
# => 683 

# We can do bit wise operation in Python too.
# But read more about it on internet I’ll give some example.
x = 2
# => 2
x << 8
# => 512

x | 8
# => 10

import random

# Random provides us lot of methods for random out of the box.

random.random()
# => 0.055884424459332505
# random.random() give us random number between 0.1 – 0.9

random.randint(1, 10)
# => 8
# random.randint() takes two value – first value is starting value and second value is last value but
# it’s always excluded from the list. It will give us random integer value between both values.

myChoice = ['coffee', 'cold-coffee', 'tea', 'cold-tea', 'green-tea', 'red-tea', 'mashala-tea', 'ginger-tea']
random.choice(myChoice)
# => cold-coffee
# random.choice() give us random choice from an list/array.

myChoice = ['coffee', 'cold-coffee', 'tea', 'cold-tea', 'green-tea', 'red-tea', 'mashala-tea', 'ginger-tea']
random.shuffle(myChoice)
# => ['tea', 'mashala-tea', 'cold-coffee', 'coffee', 'ginger-tea', 'green-tea', 'red-tea', 'cold-tea']
# random.shuffle() give back shuffled list/array.

# In Python if we do calculation with decimal there are so many known problems. For example -

# If we add these numbers below –
0.1 + 0.1 + 0.1 
# => 0.30000000000000004
# we get this number but we get 4 at the end that shouldn’t be there.

# and if we subtract –
0.1 + 0.1 + 0.1 - 0.3
# => 5.551115123125783e-17
# this is wrong any math person can tell you that.

# For that we need to use Decimal (and we have to provide value is quotes) –
from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
# => Decimal('0.3')
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# => Decimal('0.0')

# Set is part of number data-types.
# Sets are define in { curly-braces }. Dictionaries are also define in 
# { curly-braces } but they are define in key-value pairs.

setone = {1, 2, 3, 4}

#intersection (for intersection we use &)
setone & {1, 3}
# => {1, 3}
# union ( for union we use | (or))
setone | {1, 3, 7}
# => {1, 2, 3, 4, 7}

# important thing to know is when we take a set ant subtract all the value it
# will give us that empty-set as set() not set{} because empty {} is type dictionary.
setone - {1, 2, 3, 4}
# => set()
