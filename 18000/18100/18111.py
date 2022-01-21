import sys

n, m, b = map(int, input().split())
arr = []
d = dict()

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    arr.extend(row)
    for r in row:
        d[r] = d.get(r, 0) + 1

answer = []

for s in range(min(arr), max(arr) + 1):
    _b = b
    t = 0
    for k, v in d.items():
        if k > s:
            sub = k - s
            _b += sub * v
            t += 2 * sub * v
        elif k < s:
            sub = s - k
            _b -= sub * v
            t += sub * v

    if _b >= 0:
        answer.append([t, s])

if len(answer) > 1:
    answer.sort(key=lambda x:(x[0], -x[1]))

print(' '.join(map(str, answer[0])))