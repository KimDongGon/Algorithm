from collections import deque

n = int(input())
card = deque(x for x in range(1, n + 1))
answer = []

while card:
    c = card.popleft()
    answer.append(c)
    card.rotate(-1)

print(' '.join(map(str, answer)))