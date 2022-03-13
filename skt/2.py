from collections import deque

def solution(n, clockwise):
    arr = [[0] * n for _ in range(n)]
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def check():
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 0:
                    return False
        return True

    num = 1
    deq = deque([[-1, 0], [n - 1, -1], [n, n - 1], [0, n]])

    while True:
        if check():
            break

        row, col = deq[0]
        if arr[row + dir[0][0]][col + dir[1][1]] != 0:
            deq.appendleft(deq.pop())

        for d in dir:
            row, col = deq.popleft()
            arr[row + d[0]][col + d[1]] = num
            deq.append([row +d[0], col + d[1]])

        num += 1

    if clockwise:
        arr = [a[::-1] for a in arr]

    return arr

print(solution(6, False))