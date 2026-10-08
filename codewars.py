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

# Count vowel and consonant
user_input = input('Enter the string:').lower()

vowel_letter = 'aeiou'
vowel = 0
consonant = 0

for char in user_input:
    if char.isalpha():
        if char in vowel_letter:
            vowel += 1
        else:
            consonant += 1

print(f'Vowel count: {vowel}')
print(f'Consonant count: {consonant}')