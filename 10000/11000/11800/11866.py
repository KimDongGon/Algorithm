from collections import deque

n, k = map(int, input().split())
deq = deque(x for x in range(1, n + 1))
answer = []

for _ in range(n):
    for __ in range(k - 1):
        deq.rotate(-1)
    x = deq.popleft()
    answer.append(x)

print('<' + ', '.join(map(str, answer)) + '>')