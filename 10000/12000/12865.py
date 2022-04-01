import sys

N, K = map(int, sys.stdin.readline().split())

arr = []
dp = [0] * (K + 1)

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr = sorted(arr)

for i in range(N):
    for j in range(K, arr[i][0] - 1, -1):
        dp[j] = max(dp[j - arr[i][0]] + arr[i][1], dp[j])

print(dp[K])