# Problem: Keep asking the user for input until they enter a number between 1 and 10.


while True:
    input_number = int(input("Please enter a number between 1-10 : "))
    if 1 <= input_number <= 10:
        print("Yes! given number is between 1-10")
        break
    else:
        print("Wrong number")