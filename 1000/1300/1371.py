import sys
cnt = [0 for _ in range(26)]

engs = sys.stdin.read()

for eng in engs:
    if eng.isalpha():
        cnt[ord(eng) - ord('a')] += 1

maxC = max(cnt)

for c in range(len(cnt)):
    if cnt[c] == maxC:
        print(chr(ord('a') + c), end='')