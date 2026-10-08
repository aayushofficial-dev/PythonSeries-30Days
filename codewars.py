# Character Frequency
# Write a Python program that takes a string and counts how many times each character appears.

user_input = input('Enter the string:')

result = {}

for i in user_input:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

print(result)

