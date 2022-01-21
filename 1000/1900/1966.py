from collections import deque

t = int(input())

answer = []

for i in range(t):
    n, m = map(int, input().split())
    arr = deque(list(map(int, input().split())))

    c = 0
    while True:
        if max(arr) > arr[0]:
            arr.rotate(-1)
            if m == 0:
                m = len(arr) - 1
            else:
                m -= 1
        else:
            c += 1
            arr.popleft()
            if m == 0:
                break
            else:
                m -= 1
    answer.append(c)

for a in answer:
    print(a)