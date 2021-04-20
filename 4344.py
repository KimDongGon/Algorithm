a = int(input())
for i in range(0, a):
    b = list(map(int, input().split()))
    avg = (sum(b) - b[0]) / b[0]
    cnt = 0
    for j in range(1, len(b)):
        if b[j] > avg:
            cnt += 1
    print(f'{format((cnt / b[0]) * 100, ".3f")}%')