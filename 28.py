string = input()
list(string.lower())
count = 0

for i in string:
    if i in 'aeiou':
        count+=1

print(count)