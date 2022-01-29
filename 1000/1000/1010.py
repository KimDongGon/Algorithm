from math import comb
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    if n > m:
        print(comb(n, m))
    else:
        print(comb(m, n))