from itertools import combinations as cb

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

answer = sorted(list(set(cb(arr, m))))

for a in answer:
    print(' '.join(map(str, a)))