from itertools import combinations_with_replacement as cb

n, m = map(int, input().split())
arr = [x for x in range(1, n + 1)]
answer = set()

for a in cb(arr, m):
    answer.add(tuple(sorted(a)))

for a in cb(arr, m):
    print(' '.join(map(str, a)))