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