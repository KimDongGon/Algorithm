from itertools import permutations as p

n, m = map(int, input().split())

arr = [x for x in range(1, n + 1)]

for i in p(arr, m):
    print(' '.join(map(str, i)))