#1. Write a Python program to create a list of integers and then append a new integer to the end of the list.
a = [1, 2, 3, 4, 5]
print(a) # printing without appending value
a.append(7)
print(a) # printing value after appending


#2. Write a Python program to create a nested list of strings and then print the first element of the second list. 
nested_list = [[1, 2, 3, 4], 
               [5, 6, 7],
               [8, 9],
               [10]
            ]
result = nested_list[1][0]
print(result)
print(len(nested_list[1]))

    # To find the index of every item using loop and enumerate function
lst = [1, 2, 3 , 5, 4]
for index, l in enumerate(lst):
    print(f'Index: {index}, Value: {l}')


# anagrams
a = input('Enter the first word:')
b = input('Enter the second word:')

for char in a:
    if char not in b:
        print('It is not anagram.')
else:
    print('It is anagram.')

# count vowel
a = input('Enter the word:')

vowel = 'aeiou'
vowel_count = 0

for i in a:
    if i in vowel:
        vowel_count += 1

print(vowel_count)



a = input('Enter what ever you want:')

print(f"Let me provide you the multiplication table of {a}")

for i in range(1, 11):
    print(f"{a} * {i} = {a*i}")


# walrus operator 
numbers = [1,2,3,4,5]

if (count := len(numbers)) > 3:
    print(f'List has {count} elements')