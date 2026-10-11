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

# number = int(input('Enter the number:'))

# diff = number - 17

# if number > 17:
#     print(diff * 2)
# else:
#     print(diff)

# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
# a = int(input('Enter the first integer:'))
# b = int(input('Enter the second integer:'))
# result = a + b

# if result > 15 and result < 20:
#     print(20)
# else:
#     print(result)

# Write a program that takes the name and age of the user as input and displays a message whether
# the user is eligible to apply for a driving license or not.  (The eligible age is 18 years).

# name = input('Enter your name:')
# age = int(input('Enter your age:'))

# if age >= 18:
#     print(f'Hey! {name}! You are eligible for the license.')
# else:
#     print(f'Hey! {name}! You are not eligible for the license.')

'''
(a) The user enters either 'A', 'B', or 'C'. If 'A' is entered, the program should display 
the word 'Apple'; if 'B' is entered, it displays 'Banana'; and if 'C' is entered, 
it displays 'Coconut'. Use nested if statements for this.
'''

# user_input = input('Enter the A, B or C:')

# if user_input == 'A':
#     print('Apple')
# elif user_input == 'B':
#     print('Banana')
# elif user_input == 'C':
#     print('coconut')
# else:
#     print('Invalid input!')

'''
A student enters the number of college credits earned. If the number of credits is greater than 
or equal to 90, 'Senior Status' is displayed; if greater than or equal to 60, 'Junior Status' 
is displayed; if greater than or equal to 30, 'Sophomore Status' is displayed; else, 'Freshman Status'
is displayed.
'''
# credit = int(input('Enter the credit earned:'))

# if credit >= 90 and credit <= 100:
#     print('Senior status.')
# elif credit >= 60:
#     print('Junior status.')
# elif credit >= 30:
#     print('Sophomore Status')
# else:
#     print('Freshman Status.')

"""
 The user enters a number. If the number is divisible by 3, the word 'Fizz'
 should be displayed; if the number is divisible by 5 the word 'Buzz' should be displayed 
 and if the number is divisible by both 'FizzBuzz' should be displayed.
"""
# number = int(input('Enter the number:'))

# if number % 3 == 0 and number % 5 == 0:
#     print('FizzBuzz')
# elif number % 5 == 0:
#     print('Buzz')
# elif number % 3 == 0:
#     print('Fizz')
# else:
#     print('Not divisible by 3 and 5.')

age = 20

if age < 13:
    print('Child')
elif age < 18:
    print('Teenager')
else:
    print('Adult')

# Find the smallest and largest number in a list and return their sum. The list will always have at least
# two elements.
def min_max_sum(input):
    for i in range(len(input)):
        min_num = min(input)
        max_num = max(input)
    return min_num + max_num
print(min_max_sum([1, 2, 3, 4, 5]))  # Output: 6

def min_max_sum(numbers):
    smallest = numbers[0]
    largest = numbers [0]

    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return smallest + largest
print(min_max_sum([1, 2, 3, 4, 5]))