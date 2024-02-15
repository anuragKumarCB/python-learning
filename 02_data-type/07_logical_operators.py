x = 2
y = 3
z = 4

# logical operators are binary operators that need two operands to do the operation.
# logical operators can be used even on Boolean value themselves.

# and operator -
x < y and y < z     # (x is less than y and y is less than z)
# True and y < z    # (first is true)
# True and True     # (second is ture)
# => true           # (both are true so true)
# if both value are true then and operators will return true,
# if either of the value is false then it will return false

#  or operator -
x > y or y < z      # (x is greter than y or y is less than z)
# False or y < z    # (firs is false)
# False or True     # (second is true)
# True              # ( right side will execute)
# or operator behave little different. if left side value is true then lef will execute.
# if right side value is true then right will execute.
# if both side is false then it will not execute and if both side is true then it will execute.

if x > y or y < z:
    print("right-side")

if x < y or y > z:
    print("left-side")

if x < y or y < z:
    print("both-true")