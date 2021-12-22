t = int(input())
answer = []
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def dfs(maps, x, y, m, n):
    stack = [[x, y]]
    maps[y][x] = 0
    while stack:
        _x, _y = stack.pop()
        for d in directions:
            if 0 <= _x + d[0] <= m - 1 and 0 <= _y + d[1] <= n - 1 and maps[_y + d[1]][_x + d[0]] == 1:
                maps[_y + d[1]][_x + d[0]] = 0
                stack.append([_x + d[0], _y + d[1]])


for _ in range(t):
    m, n, k = map(int, input().split())
    maps = [[0 for i in range(m)] for j in range(n)]
    coordis = []

    c = 0
    for __ in range(k):
        x, y = map(int, input().split())
        coordis.append([x, y])
        maps[y][x] = 1

    for coordi in coordis:
        x, y = coordi
        if maps[y][x] == 1:
            dfs(maps, x, y, m, n)
            c += 1

    answer.append(c)

for _answer in answer:
    print(_answer)