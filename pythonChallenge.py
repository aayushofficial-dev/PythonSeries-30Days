'''
# Unique Sum
Get a sum of all numbres from a list that are unique. If a number appears in the list more than
once, do not include it in the total sum.
'''

def unique_sum(number):
    result = 0
    for num in number:
        if number.count(num) == 1:
            result += num
    return result

print(unique_sum([1, 2, 3]))


'''
# Min Max sum
Find the smallest and largest number in a list and reutrn their sum. The list will always have 
at least two elements.
'''

print('Using loop...')
def min_max_sum(number):
    min_num = number[0]
    max_num = number[0]

    for num in number:
        if num > min_num:
            min_num = num
        elif num < max_num:
            max_num = num
    return min_num + max_num
print(min_max_sum([2, 3, 4, 7]))

print('Using built-in function..')
def min_max_sum(input):
    min_num = min(input)
    max_num = max(input)
    return min_num + max_num
print(min_max_sum([2, 3, 4, 7]))

'''
# Balanced Strings
Write a function that checks if two strings are balanced. Two strings are balanced if all characters from the first
string are also present in the second one. the position of the characters does not matter, they do not have to be 
consecutive. Return a boolean value.
'''

def balanced_string(a, b):
    for char in a:
        if char not in b:
            return False
    return True
print(balanced_string('apn', 'japan'))


'''
# Reversed a String
Write a function that reverse all characters of a string.
'''
def reverse(input):
    return input[::-1]
print(reverse('aayush'))

print('Using loop...')
def reverse(input):
    result = ''
    for i in input:
        result = i + result
    return result
print(reverse('aayush'))