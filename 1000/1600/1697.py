from collections import deque

n, k = map(int, input().split())

deq = deque([[n, 0]])
visited = set()
if n == k:
    print(0)
else:
    while deq:
        d, t = deq.popleft()
        w = [2 * d, d + 1, d - 1]

        for _w in w:
            if _w == k:
                print(t + 1)
                deq.clear()
                break
            if _w not in visited and 0 <= _w <= 100000:
                deq.append([_w, t + 1])
                visited.add(_w)
