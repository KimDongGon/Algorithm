import sys
import heapq

N = int(sys.stdin.readline())
hq = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if hq:
            num = heapq.heappop(hq)
            print(num)
        else:
            print(0)
    else:
        heapq.heappush(hq, x)