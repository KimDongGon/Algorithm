import sys

k, n = map(int, input().split())

arr = []

for _ in range(k):
    arr.append(int(sys.stdin.readline()))

start, end = 0, max(arr)
i = end // 2 + 1
answer = []

while start <= end:
    if i == 0:
        i = 1
        break
    s = [x // i for x in arr]
    if sum(s) >= n:
        start = i + 1
        i = (start + end) // 2
    else:
        end = i - 1
        i = (start + end) // 2

print(i)