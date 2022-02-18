arr = [[0] * 101 for _ in range(101)]
answer = 0

for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            arr[c][r] = 1

for a in arr:
    for _a in a:
        if _a == 1:
            answer += 1

print(answer)