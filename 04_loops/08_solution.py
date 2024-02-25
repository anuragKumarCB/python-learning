# Problem: Check if a number is prime.

# get a number from user
input_number = int(input("Enter a number : "))
# assume its orime number
is_prime = True

if input_number <=3:
    is_prime = True

elif (input_number % 2) == 0 or (input_number % 3) == 0:
    is_prime = False

else:
    is_prime = True

if is_prime:
    print(f"Given number {input_number} is Prime number")
    
else:
    print(f"Given number {input_number} is not a Prime number")