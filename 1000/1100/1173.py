N, m, M, T, R = map(int, input().split())
answer = 0
curT = 0
curM = m

if m + T > M:
    answer = -1
else:
    while curT != N:
        if curM + T <= M:
            curM += T
            curT += 1
        else:
            curM -= R
            if curM < m:
                curM = m
        answer += 1

print(answer)