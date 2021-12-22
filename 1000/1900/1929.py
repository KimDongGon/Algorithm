m, n = map(int, input().split())
arr = [i for i in range(n + 1)]

for i in range(2, int((n + 1) ** (1 / 2)) + 1):
    if arr[i] == 0:
        continue
    for j in range(i + i, n + 1, i):
        arr[j] = 0

arr = [k for k in arr if (k != 0 and k != 1) and k >= m]

for a in arr:
    print(a)