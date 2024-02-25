# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# take input from user
person_age = input("Please provide you age: ")
# when we get data using input method its datatype is string. so, we have to convert it to string
person_age_in_int = int(person_age)

# (condition for age group)

# check for invalid age (0 and negative value)
if person_age_in_int < 0:
    print("Invalid age. Please prvoide age above 0 year")

elif person_age_in_int < 13:
    print("Child")

elif person_age_in_int < 20:
    print("Teenager")

elif person_age_in_int < 60:
    print("Adult")

else:
    print("Senior")