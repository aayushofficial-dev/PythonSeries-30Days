# Find the second highest num from the list.

number = [1, 2, 3, 4, 5]

largest = number[0]
second_largest = number[0]

for num in number:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num < largest:
        second_largest = num

print(second_largest)

'''
Suppose you are working on a project to develop a simple calculator program in Python.
The user is prompted to enter two numbers and then select an operation (addition, 
subtraction, multiplication, or division). You have already implemented the logic 
for each operation, but now you need to implement a loop to allow the user to perform 
multiple calculations without having to restart the program each time.
Write a Python program that uses a loop to repeatedly prompt the user for two numbers 
and an operation, perform the calculation, and display the result. The program should 
continue looping until the user enters "q" to quit the program.
'''

# while True:
#     print('Calculator...')
#     print('1. Addition')
#     print('2. Subtraction')
#     print('3. Multiplication')
#     print('4. Division')
#     print('5. Exit')

#     a = int(input('Enter the first number:'))
#     b = int(input('Enter the second number:'))

#     choice = input('What you want to perform?:')

#     # condition
#     if choice == '1':
#         print(f'The addition of {a} and {b} is {a + b}')
#     elif choice == '2':
#         print(f'The subraction of {a} and {b} is {a - b}')
#     elif choice == '3':
#         print(f'The multiplication of {a} and {b} is {a * b}')
#     elif choice == '4':
#         if b == 0:
#             print('Number cannot be divided by 0.')
#         else:
#             print(f'The division of {a} and {b} is {a / b}')
#     elif choice == '5':
#         print('Thank you for using the program.')
#         break
#     else:
#         print('Invalid input! Please try again!')

'''
Suppose you are working on a program that simulates a game of dice where the player rolls two six-sided 
dice and tries to guess the total value. You have already implemented the logic to generate random dice
rolls and compare them to the player's guess, but now you need to implement a loop to allow the player 
to play multiple rounds without having to restart the program each time. 
'''
import random

print('Dice guessing game..')

while True:
    user_input = int(input('Guess the total of 2 dice (2-12):'))

    dice1 = random.randint(1, 7)
    dice2 = random.randint(1, 7)
    total = dice1 + dice2

    if user_input == total:
        print(f'Congratulations! You have guessed the total correct {total}')
    elif user_input < total:
        print('You guessed it low!')
    elif user_input > total:
        print('You guessed it high!')
    else:
        print('Invalid input!')

    play_again = input('Play again?(y/n):')

    if play_again.lower() == 'n':
        print('Thank you for playing the game.')
        break

    