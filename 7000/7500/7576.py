from collections import deque

m, n = map(int, input().split())

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

maps = []
deq = deque()

for i in range(n):
    row = list(map(int, input().split()))
    maps.append(row)
    k = [j for j, v in enumerate(row) if v == 1]
    for _k in k:
        deq.append([_k, i])

def bfs(maps, deq):
    day = 0
    while deq:
        l = len(deq)
        for _ in range(l):
            x, y = deq.popleft()
            for d in directions:
                if 0 <= x + d[0] <= m - 1 and 0 <= y + d[1] <= n - 1 and 0 == maps[y + d[1]][x + d[0]]:
                    maps[y + d[1]][x + d[0]] = 1
                    deq.append([x + d[0], y + d[1]])
        day += 1

    if any(0 in m for m in maps):
        return -1
    else:
        return day - 1

print(bfs(maps, deq))