import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    M = int(sys.stdin.readline())
    hq = []
    for __ in range(M):
        s = sys.stdin.readline().strip().split()

        if s[0] == 'I':
            num = int(s[1])
            heapq.heappush(hq, num)
        elif s[0] == 'D':
            if hq:
                if s[1] == '1':
                    hq.remove(heapq.nlargest(1, hq)[0])
                elif s[1] == '-1':
                    heapq.heappop(hq)
    if hq:
        print(hq[-1], hq[0])
    else:
        print('EMPTY')