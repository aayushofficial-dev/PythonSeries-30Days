# Develop a program that asks the user for a number and then displays whether the number is positive or negative.
# number = int(input('Enter the number:'))

# if number > 0:
#     print('It is a positive number.')
# else:
#     print('It is a negative number.')

# Write a Python program that reads in two numbers and prints out whether their sum is even or odd.
# a = int(input('Enter the first number:'))
# b = int(input('Enter the second number:'))

# result = a + b
# if result % 2 == 0:
#     print(f'{result} is a even number.')
# else:
#     print(f'{result} is a odd number.')

# Write a program to find the lowest number out of two numbers expected from the user. 
# a = int(input('Enter the first number:'))
# b = int(input('Enter the second number:'))

# if a < b:
#     print(f'{a} is the smallest number.')
# else:
#     print(f'{b} is the smallest number.')


# Write a program to check whether a character is a vowel or consonant. [Expected from user’s input].
# a = input('Enter a character:').lower()
# vowel = 'aeiou'

# if a in vowel:
#     print('It is a vowel letter.')
# else:
#     print('it is a consonant letter.')

# Give an appropriate if statement for each of the following
# (the value of num is not important):
# (a) Displays 'within range' if num is between 0 and 100, inclusive.
# (b) Displays 'within range' if num is between 0 and 100, inclusive, and displays 'out of range' otherwise.

# num = int(input('Enter the number:'))

# if num > 0 and num < 100:
#     print('within range')
# else:
#     print('out of range')

# Write a Python program to calculate the difference between a given number and 17.
#  If the number is greater than 17, return twice the absolute difference.

number = int(input('Enter the number:'))

diff = number - 17

if number > 17:
    print(diff * 2)
else:
    print(diff)

# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
a = int(input('Enter the first integer:'))
b = int(input('Enter the second integer:'))
result = a + b

if result > 15 and result < 20:
    print(20)
else:
    print(result)

# Write a program that takes the name and age of the user as input and displays a message whether
# the user is eligible to apply for a driving license or not.  (The eligible age is 18 years).

name = input('Enter your name:')
age = int(input('Enter your age:'))

if age >= 18:
    print(f'Hey! {name}! You are eligible for the license.')
else:
    print(f'Hey! {name}! You are not eligible for the license.')