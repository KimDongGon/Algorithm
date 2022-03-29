N = int(input())
arr = list(map(int, input().split()))
sortedArr = sorted(list(set(arr)))

d = dict()

for i, a in enumerate(sortedArr):
    d[a] = i

answer = []

for a in arr:
    answer.append(d[a])

print(' '.join(map(str, answer)))