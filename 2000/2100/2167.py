n, m = map(int, input().split())
arr = []
dp = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

k = int(input())

answer = []

for _ in range(k):
    i, j, x, y = map(int, input().split())
    answer.append(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])

for _a in answer:
    print(_a)