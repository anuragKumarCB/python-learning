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