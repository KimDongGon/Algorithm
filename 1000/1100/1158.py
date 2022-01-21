from collections import deque

n, k = map(int, input().split())

arr = deque(x for x in range(1, n + 1))

answer = []

for _ in range(n):
    for i in range(k - 1):
        arr.rotate(-1)
    answer.append(arr.popleft())

print('<' + ', '.join(map(str, answer)) + '>')