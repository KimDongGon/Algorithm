N = int(input())
names = list(input() for _ in range(N))
count = [0 for _ in range(26)]
for name in names:
    count[ord(name[0]) - ord('a')] += 1

if max(count) < 5:
    print('PREDAJA')
else:
    for i in range(len(count)):
        if count[i] >= 5:
            print(chr(ord('a') + i), end='')