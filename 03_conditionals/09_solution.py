# Problem: Determine if a year is a leap year. (Leap years
# are divisible by 4, but not by 100 unless also divisible by 400).

# get the year and convert it to integer
provided_year = input("Please provide a year : ")
year_in_int = int(provided_year)

# check for leap year
# if this year is divisible by 100 then its not leap year

if (year_in_int % 400 == 0) or (year_in_int % 4 == 0 and year_in_int % 100 != 0):
    print(f"provided year {provided_year} is a leap year")
else:
    print(f"provided year {provided_year} is not leap year")

