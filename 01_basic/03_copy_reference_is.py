var1 = [1,2,3]
var2 = var1
var1[0] = 55
print(var1)
print(var2)
# both variable reflect chnages because both have same reference (it's not about same value)
print("-----------------")
variable1 = [1,2,3]
variable2 = variable1
variable1 = [1,2,3]
# variable1[0] = 55
print(variable1)
print(variable2)
# here both varibale is reflecting different even though they were having same reference but after reassigning same value there was
# they are now pointing to different memeory-space (even though they have same value)

# to check if both variable have same reference
print(var1 == var2)
print(var1 is var2)

print("------------")

print(variable1 == variable2)
print(variable1 is variable2)

# == check if both variables have same value and is operator check if both variables are pointing to same reference