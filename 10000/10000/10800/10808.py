c = [0] * 26

s = input()

for _s in s:
    c[ord(_s) - ord('a')] += 1

print(' '.join(map(str, c)))