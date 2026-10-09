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

