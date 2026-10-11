# Membership operator
color = ['red', 'green', 'white']

if 'green' in color:
    print('True')
else:
    print('False')

'''Using function'''
def color(name):
    if 'red' in name:
        return True
    else:
        return False
print(color(['red', 'green', 'white']))

x = 20

y = [10, 20, 30]

print(x in y)

print('Using while loop')
i = 1 
while i <= 10:
    print(i, "hello world")
    i += 1

print('Using for loop')
for i in range(1, 11):
    print(i, "Hello world")

print('Using function')
def program(message):
    for i in range(1, 11):
        print(i, message)
print(program('hello world'))


#1. Write a program to print numbers from 1 to 10. 
print('number from 1 to 10')
for i in range(1, 11):
    print(i)

#2. Write a program to print all odd numbers between 1 and 15.
print('odd number between 1 and 15')
for i in range(1, 16):
    if i % 2 != 0:
        print(i)

#3. Write a program to calculate the sum of the first 10 natural numbers. 
print('Sum of first 10 natural numbers.')
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

#  Write a program that prompts the user to input a positive integer.
#  It should then print the multiplication table of that number up to 10.

# num = int(input('Enter the number:'))

# if num > 0:
#     print(f'Multiplication table of {num}:')
#     for i in range(1, 11):
#         print(f'{num} * {i} = {num * i}')
# else:
#     print('Cannot print the table of negative number.')



