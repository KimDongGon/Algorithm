n = int(input())

arr = []

dp = [0] * n

for _ in range(n):
    arr.append(int(input()))

if n == 1 or n == 2:
    print(sum(arr))
elif n == 3:
    print(max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2]))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])
    for i in range(3, n):
        dp[i] = max(arr[i] + max(dp[i - 2], dp[i - 3] + arr[i - 1]), dp[i - 1])
    print(max(dp))