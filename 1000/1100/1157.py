a = input().lower()
count = [0] * 26
max = 0
for i in range(0, len(a)):
    index = ord(a[i]) - ord('a')
    count[index] += 1
    if count[index] > max:
        max = count[index]
if count.count(max) > 1:
    print('?')
else:
    print(chr(count.index(max) + ord('a')).upper())