from itertools import combinations as cb

n, m = map(int, input().split())

arr = [x for x in range(1, n + 1)]

for c in cb(arr, m):
    print(" ".join(map(str, c)))