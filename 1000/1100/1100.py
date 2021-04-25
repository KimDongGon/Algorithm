import sys
chess = list(sys.stdin.readline() for _ in range(8))
cnt = 0
for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:
                cnt += 1 if (chess[i])[j] == 'F' else 0
            else:
                continue
    else:
        for j in range(8):
            if j % 2 == 0:
                continue
            else:
                cnt += 1 if (chess[i])[j] == 'F' else 0

print(cnt)