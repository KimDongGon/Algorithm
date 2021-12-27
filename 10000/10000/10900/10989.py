import sys
n = int(sys.stdin.readline())

d = dict()

for _ in range(n):
    k = int(sys.stdin.readline())
    d[k] = d.get(k, 0) + 1

for i in range(1, 10001):
    if d.get(i, 0) != 0:
        for j in range(d[i]):
            print(i)