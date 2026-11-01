a = 'abcdefghijklmnopqrstuvwxyz'
for index, a in enumerate(a, start=1):
    print(index, a)

fav_lang = ["Python", "Django", "HTML", "SQL"]

for index, language in enumerate(fav_lang, start=1):
    if language == "HTML":
        continue
    print(index, language)

print(fav_lang)

# Replace every element in the list with its index position:
numbers = [10, 20, 30, 40, 50]

result = []

for i in range(len(numbers)):
    result.append(i)

print(result)

#1. Write a python program to prompt the user for input number and print square of that particular integer.
num = int(input('Enter the number:'))
square = num * num
print(square)

#2. Write a python program to display the circumference of a circle. (import math module)
import math

radius = int(input('Enter the number:'))
c_of_circle = 2 * math.pi * radius
print(c_of_circle)

#3. Write a python program to ask in kilograms and convert into grams.
kg = int(input('Enter tke kilograms:'))
grams = kg * 1000
print(grams)

#4. Write a python program to display the area of the triangle. 
base = int(input('Enter the base of the triangle:'))
height = int(input('Enter the height of the triangle:'))

area = 0.5 * base * height
print(f'The area of the triangle of {base} and {height} if {area}')

# 5. Write a python program to prompt user to input their name and display 
name = input('Enter your name:')

print(f'Hello {name}')

# PART 3
#1. Write a python program to find the remainder of a given number if divisor is 2.
number = int(input('Enter the number:'))

remainder = number % 2
print(f'The remainder is {remainder}')

# Demonstrate the use of ord() and chr() functions using a simple python program. [Take Data From User’s]
'''ord value:
The ord function: gives the UTF-8 (ASCII) encoding of a given character. For example,
ord('A) is 65
'''
ord_value = input('Enter the value:')
char_value = ord(ord_value)
print(char_value)

'''chr_value: 
The chr function: gives the character for a given encoding value, thus 
chr(65) is 'A'
'''
chr_value = int(input('Enter the value:'))
ord_value = chr(chr_value)
print(ord_value)

# time conversion: Write a python program to convert seconds into hours, minutes and seconds.
late_in_sec = 13445

sec_into_min = late_in_sec % 60
min_into_hour = (late_in_sec // 60) % 60
hours = late_in_sec // 3600

print(f"{hours} hours, {min_into_hour} minutes, {sec_into_min} seconds")

'''
Implicit type conversion: Python converts the type automatically.
---> Implicit type conversion happens when Python automatically converts a value to another compatible type.

Important: Python does not automatically convert every incompatible type.
For example, "10" + 5 raises a TypeError.
'''
a = 10
b = 2.5

result = a + b
print(result)
print(type(result))

'''
Explicit type conversion
---> Explicit conversion happens when you tell Python to convert a value yourself.

Note that not every conversion is valid. For example, int("hello") raises a ValueError.
'''
a = '10'

b = int(a)

print(b)
result = b + 5
print(result)
print(type(result))

