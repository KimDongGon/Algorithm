import sys
n, m = map(int, sys.stdin.readline().split())

d = dict()
arr = []

for _ in range(n):
    name = sys.stdin.readline().strip()
    d[name] = 1

answer = 0

for _ in range(m):
    name = sys.stdin.readline().strip()
    if d.get(name, 0) == 1:
        answer += 1
        arr.append(name)

print(answer)
arr.sort()
for a in arr:
    print(a)