r, c = map(int, input().split())
k = int(input())

arr = [[0] * (c + 1) for _ in range(r + 1)]
dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]
index = {
    0: 1,
    1: 2,
    2: 3,
    3: 0
}

arr[1][1] = 1
if k > r * c:
    print(0)
else:
    row = 1
    col = 1
    idx = 0
    cnt = 0
    while True:
        if cnt == k - 1:
            break
        _r = row + dir[idx][0]
        _c = col + dir[idx][1]

        if 1 <= _r <= r and 1 <= _c <= c:
            if arr[_r][_c] == 0:
                arr[_r][_c] = 1
                row = _r
                col = _c
                cnt += 1
            else:
                idx = index[idx]
        else:
            idx = index[idx]
    print(row, col)