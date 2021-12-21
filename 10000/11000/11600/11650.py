n = int(input())
c = []
for i in range(n):
    x, y = map(int, input().split())
    c.append([x, y])

c = sorted(c, key=lambda k: (k[0], k[1]))

for _c in c:
    print(_c[0], _c[1])