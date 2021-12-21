n, m = map(int, input().split())

answer = 32

wf = ['W', 'B']
bf = ['B', 'W']

chess = []

for _ in range(n):
    row = input()
    chess.append(row)

for i in range(n - 1, 6, -1):
    for j in range(m - 1, 6, -1):
        w_count, b_count = 0, 0
        for k in range(i - 7, i + 1):
            for l in range(j - 7, j + 1):
                if k % 2 == 0:
                    if wf[l % 2] != chess[k][l]:
                        w_count += 1
                    if bf[l % 2] != chess[k][l]:
                        b_count += 1
                else:
                    if wf[(l + 1) % 2] != chess[k][l]:
                        w_count += 1
                    if bf[(l + 1) % 2] != chess[k][l]:
                        b_count += 1
        answer = min(answer, w_count, b_count)

print(answer)