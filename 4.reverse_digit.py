"""
Write a program that takes an integer as input and returns an integer with
reversed digit ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.
"""


# Solution

def reverse_number(number):

    # Assign -1 or 1
    if number < 0:
        negative_or_positive = -1
    else:
        negative_or_positive = 1

    # Convert to absolute value
    number = abs(number)

    # Convert number to str then to int
    reversed_number = int(str(number)[::-1])

    return negative_or_positive * reversed_number


# Pass in random numbers as arguments
print(reverse_number(500))  # 5
print(reverse_number(-56))  # -65
print(reverse_number(-90))  # -9
print(reverse_number(19))  # 91
print(reverse_number(-760))  # 67
print(reverse_number(44760))  # 6744
print(reverse_number(1))  # 1
print(reverse_number(-500))  # -5
