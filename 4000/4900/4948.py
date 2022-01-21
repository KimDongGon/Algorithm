num = [True] * (123456 * 2 + 1)

for i in range(2, 123456 * 2 + 1):
    for j in range(i + i, 123456 * 2 + 1, i):
        if num[j]:
            num[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    print(len([x for x in num[n + 1:2 * n + 1] if x]))