from collections import deque

n = int(input())
deq = deque()
answer = []

for _ in range(n):
    s = input()
    if len(s.split()) == 2:
        k = list(s.split())
        if k[0] == 'push_front':
            deq.appendleft(int(k[1]))
        elif k[0] == 'push_back':
            deq.append(int(k[1]))
    else:
        if s == 'pop_front':
            if len(deq) == 0:
                answer.append(-1)
            else:
                x = deq.popleft()
                answer.append(x)
        elif s == 'pop_back':
            if len(deq) == 0:
                answer.append(-1)
            else:
                x = deq.pop()
                answer.append(x)
        elif s == 'size':
            answer.append(len(deq))
        elif s == 'empty':
            if len(deq) == 0:
                answer.append(1)
            else:
                answer.append(0)
        elif s == 'front':
            if len(deq) == 0:
                answer.append(-1)
            else:
                answer.append(deq[0])
        elif s == 'back':
            if len(deq) == 0:
                answer.append(-1)
            else:
                answer.append(deq[-1])

for a in answer:
    print(a)