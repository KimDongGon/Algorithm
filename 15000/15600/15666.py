from itertools import combinations_with_replacement as cb

n, m = map(int, input().split())

arr = sorted(list(set(map(int, input().split()))))

for a in sorted(cb(arr, m)):
    print(' '.join(map(str, a)))