from collections import deque;

w, h = map(int, input().split())
n = int(input())
deq = deque([[0, 0, h, w]])
for _ in range(n):
    # no 가로: 0, 세로: 1
    no, idx = map(int, input().split())
    l = len(deq)
    for i in range(l):
        r1, c1, r2, c2 = deq.popleft()
        if no == 0:
            if r1 < idx < r2:
                deq.append([r1, c1, idx, c2])
                deq.append([idx, c1, r2, c2])
            else:
                deq.append([r1, c1, r2, c2])
        elif no == 1:
            if c1 < idx < c2:
                deq.append([r1, c1, r2, idx])
                deq.append([r1, idx, r2, c2])
            else:
                deq.append([r1, c1, r2, c2])
deq = sorted(deq, key=lambda x: (x[2] - x[0]) * (x[3] - x[1]), reverse=True)
r1, c1, r2, c2 = deq[0]
print((r2 - r1) * (c2 - c1))