arr = [1, 1, 2, 2, 2, 8]
a = list(map(int, input().split()))
ans = []
for i in range(0, len(arr)):
    ans.append(arr[i] - a[i])

for i in ans:
    print(i, end=' ')