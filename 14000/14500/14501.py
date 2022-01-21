n = int(input())

arr = []
answer = 0

for i in range(n):
    t, p = map(int, input().split())
    arr.append([t, p])

dp = [0] * (n + 1)

for i in range(n):
    if i + arr[i][0] <= n:
        dp[i + arr[i][0]] = max(dp[i + arr[i][0]], dp[i] + arr[i][1])
    dp[i + 1] = max(dp[i], dp[i + 1])

print(max(dp))