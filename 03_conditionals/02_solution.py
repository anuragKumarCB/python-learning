# Problem: Movie tickets are priced based on age: $12 for adults (18 and over),
# $8 for children. Everyone gets a $2 discount on Wednesday.

# first check for today's day
from datetime import date
import calendar
today_date = date.today()
today_day = calendar.day_name[today_date.weekday()]

# get person age and convert it to integer
person_age = input("Please provide your age : ")
person_age_in_int = int(person_age)

# define ticket price based on age
ticket_price = 12 if person_age_in_int  >= 18 else 8
# we can change variable value based on some condition in when defining
# variable using single line if else

# if Wednesday then do the discount
if today_day == "Wednesday":
    ticket_price = ticket_price - 2

print("Ticket price for you will be $", ticket_price)