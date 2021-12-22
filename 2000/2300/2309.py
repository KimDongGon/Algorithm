from itertools import combinations as cb

talls = []

for _ in range(9):
    t = int(input())
    talls.append(t)

for c in cb(talls, 7):
    if sum(c) == 100:
        answer = c
        break

for a in sorted(answer):
    print(a)