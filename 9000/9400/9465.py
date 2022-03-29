T = int(input())

for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(2)]

    if n == 1:
        print(max(arr[0][0], arr[1][0]))
    elif n == 2:
        print(max(arr[0][0] + arr[1][1], arr[0][1] + arr[1][0]))
    else:
        dp = [[0] * n for i in range(2)]

        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[0][1] = arr[0][1] + arr[1][0]
        dp[1][1] = arr[0][0] + arr[1][1]

        for i in range(2, n):
            dp[0][i] = arr[0][i] + max(dp[1][i - 2], dp[1][i - 1])
            dp[1][i] = arr[1][i] + max(dp[0][i - 2], dp[0][i - 1])

        print(max(dp[0][n - 1], dp[1][n - 1]))