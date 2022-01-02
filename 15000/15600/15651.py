from itertools import product as p

n, m = map(int, input().split())

arr = [x for x in range(1, n + 1)]

for a in p(arr, repeat=m):
    print(' '.join(map(str, a)))