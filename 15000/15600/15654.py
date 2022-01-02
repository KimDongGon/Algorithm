from itertools import permutations as p

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for a in p(arr, m):
    print(' '.join(map(str, a)))