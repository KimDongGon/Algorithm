N = int(input())
arr = []
blue = 0
white = 0

for _ in range(N):
    arr.append(list(map(int, input().split())))

def check(row, col, n):
    bCount = 0
    wCount = 0

    for i in range(row, row + n):
        for j in range(col, col + n):
            if arr[i][j] == 1:
                bCount += 1
                if wCount != 0:
                    break
            if arr[i][j] == 0:
                wCount += 1
                if bCount != 0:
                    break

    if wCount == 0 or bCount == 0:
        return True
    return False

def solve(row, col, n):
    if n == 1 or check(row, col, n):
        global blue
        global white
        if arr[row][col] == 1:
            blue += 1
        else:
            white += 1
        return

    solve(row, col, n // 2)
    solve(row, col + n // 2, n // 2)
    solve(row + n // 2, col, n // 2)
    solve(row + n // 2, col + n // 2, n // 2)

solve(0, 0, N)
print(white)
print(blue)