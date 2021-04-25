N, Q = map(int, input().split())
times = [int(input()) for _ in range(N)]

questions = [int(input()) for _ in range(Q)]

for ques in questions:
    sumTime = 0
    for i in range(len(times)):
        if ques < sumTime + times[i]:
            print(i + 1)
            break
        else:
            sumTime += times[i]