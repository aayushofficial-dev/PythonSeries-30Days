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

# First Non-Repeating Character
# Write a Python program that finds the first character that appears only once in a string.
user_input = input('Enter the string:')

for char in user_input:
    if user_input.count(char) == 1:
        print(f'The first non-repeating character is: {char}')
        break
else:
    print('No non-repeating character is found.')

# Find the Second-Largest Number
# Write a Python program that finds the second-largest unique number in a list without using sort() or sorted().
num = [1, 2, 3, 4, 5]

largest = None
second_largest = None

for n in num:
    if largest is None or n > largest:
        second_largest = largest
        largest = n
    elif n < largest and (second_largest is None or n > second_largest):
        second_largest = n

print(second_largest)

# Sentence smash: this program smash the list into one sentence
def smash(words):
    return ' '.join(words)
print(smash(['this', 'is', 'me', 'aayush']))

def smash(words):
    result = ' '
    for word in words:
        result += word + ' '
    return result.strip()
print(smash(['this', 'is', 'me', 'aayush']))

def smash(words):
    result = ''
    for word in words:
        if result: # checks whether result already contains text.
            result += ' ' # add a space only between words
        result += word
    return result
print(smash(['this', 'is', 'me', 'aayush']))

# opposite : basically this program change the positive number into negative and vice versa
def opposite(number):
    return -number
print(opposite(1))


# reverse
def digitize(n):
    return list(map(int, reversed(str(n))))
print(digitize(12345))

# greet: this function print the famous 'hello world!'
def greet():
    return 'Hello world!'
print(greet())

# invert: this program basically check the list and if there is negative number, it changes into positive and vice versa.
def invert(lst):
    return [-x for x in lst]
print(invert([1, 2, -3, 4, -5]))

# using loop
def invert(lst):
    result = []
    for x in lst:
        result.append(-x)
    return result
print(invert([1, 2, -3, 4, -5]))
