t = int(input())
money = []
answer = []

m = [25, 10, 5, 1]

for _ in range(t):
    k = int(input())
    money.append(k)

for _money in money:
    temp = []
    for _m in m:
        temp.append(_money // _m)
        _money = _money % _m
    answer.append(temp)

for a in answer:
    print(' '.join(map(str, a)))