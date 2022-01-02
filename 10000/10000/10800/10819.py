from itertools import permutations as p

n = int(input())
arr = map(int, input().split())
answer = 0
for a in p(arr, n):
    temp = 0
    for i in range(1, n):
        temp += abs(a[i] - a[i - 1])
    if answer < temp:
        answer = temp

print(answer)