n, m = map(int, input().split())
a = []
for _ in range(n):
    _a = list(map(int, input().split()))
    a.append(_a)

b = []
m, k = map(int, input().split())
for _ in range(m):
    _b = list(map(int, input().split()))
    b.append(_b)

b = list(map(list, zip(*b)))

answer = []

for _a in a:
    temp = []
    for _b in b:
        temp.append(sum([x * y for x, y in zip(_a, _b)]))
    answer.append(temp)

for a in answer:
    print(' '.join(map(str, a)))