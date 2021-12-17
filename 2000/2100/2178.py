from collections import deque

n, m = map(int, input().split())
miro = []
for _ in range(n):
    r = input()
    miro.append(list(map(int, r)))


queue = deque([[0, 0, 1]])

directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

answer = 0

while len(queue) != 0:
    x, y, count = queue.popleft()
    miro[x][y] = 0
    if x == n - 1 and y == m - 1:
        answer = count
        break
    for d in directions:
        if 0 <= x + d[0] < n and 0 <= y + d[1] < m and miro[x + d[0]][y + d[1]] == 1:
            queue.append([x + d[0], y + d[1], count + 1])
            # miro[x + d[0]][y + d[1]] = 0

print(miro)
print(answer)

