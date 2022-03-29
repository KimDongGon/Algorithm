import sys

n, m = map(int, sys.stdin.readline().split())
arr = [''] * n
d = dict()
for i in range(n):
    name = sys.stdin.readline().strip()
    arr[i] = name
    d[name] = i + 1

for _ in range(m):
    a = sys.stdin.readline().strip()
    if a.isnumeric():
        print(arr[int(a) - 1])
    else:
        print(d.get(a, 0))