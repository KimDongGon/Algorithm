from collections import deque
dir = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

def bfs(row, col):
    queue = deque([[row, col]])
    while queue:
        r, c = queue.popleft()
        for d in dir:
            _row = r + d[0]
            _col = c + d[1]
            if isIn(_row, _col) and arr[_row][_col] == 1:
                arr[_row][_col] = 0
                queue.append([_row, _col])

def isIn(row, col):
    return 0 <= row < h and 0 <= col < w

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    answer = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                answer += 1
                bfs(i, j)

    print(answer)