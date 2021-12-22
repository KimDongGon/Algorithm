xd = []
yd = []

for _ in range(3):
    x, y = map(int, input().split())
    xd.append(x)
    yd.append(y)


print([x for x in xd if xd.count(x) == 1][0], [y for y in yd if yd.count(y) == 1][0])