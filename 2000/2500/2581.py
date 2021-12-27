m = int(input())
n = int(input())

num = [1 for _ in range(n + 1)]
num[0] = 0
num[1] = 0

for i in range(2, int((n + 1) ** (1 / 2)) + 1):
    if num[i] == 0:
        continue
    for j in range(i ** 2, n + 1, i):
        num[j] = 0

answer = [i for i, x in enumerate(num) if m <= i <= n and x == 1]

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))