n = int(input())

pattern = {0: 5, 1: 3, 2: 4, 5: 0, 3: 1, 4: 2}
MAX = -1

arr = list(list(map(int, input().split())) for _ in range(n))

for k, v in pattern.items():
    _sum = 0
    up = arr[0][k]
    down = arr[0][v]

    for a in arr:
        temp = []
        for i, _a in enumerate(a):
            if _a == up:
                pos = i
            temp.append(_a)
        temp.remove(a[pos])
        temp.remove(a[pattern[pos]])
        down = a[pos]
        up = a[pattern[pos]]
        _sum += max(temp)

    MAX = max(MAX, _sum)

print(MAX)