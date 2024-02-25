# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_numbers(target_number):
    for num in range(1, target_number+1):
        if (num % 2) == 0:
            print(num)

even_numbers(48)