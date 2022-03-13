def solution(width, height, diagonals):
    answer = 0

    dp = [[0] * (height + 1) for _ in range(width + 1)]

    MOD = 10000019

    dp[0][0] = 1
    for i in range(width + 1):
        for j in range(height + 1):
            if i == 0 and j == 0:
                continue
            dp[i][j] = 0
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= MOD

    for diagonal in diagonals:
        x, y = diagonal
        cntAB = (dp[x][y - 1] * dp[width - x + 1][height - y]) % MOD

        x, y = diagonal
        cntBA = (dp[x - 1][y] * dp[width - x][height - y + 1]) % MOD

        answer += (cntAB + cntBA) % MOD

    return answer

print(solution(2, 2, [[1,1], [2,2]]))
print(solution(51, 37, [[17, 19]])) # 3225685