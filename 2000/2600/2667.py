n = int(input())

m = []
answer = []
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for _ in range(n):
    row = input()
    m.append(list(row))

def dfs(x, y):
    if m[x][y] == '0':
        return 0
    stack = [[x, y]]
    ans = 1
    m[x][y] = '0'
    while len(stack) != 0:
        _x, _y = stack.pop()
        for d in directions:
            if 0 <= _x + d[0] <= n - 1 and 0 <= _y + d[1] <= n - 1 and m[_x + d[0]][_y + d[1]] == '1':
                stack.append([_x + d[0], _y + d[1]])
                m[_x + d[0]][_y + d[1]] = '0'
                ans += 1
    return ans

for i, _m in enumerate(m):
    idx = [_idx for _idx, v in enumerate(_m) if v == '1']
    for _idx in idx:
        l = dfs(i, _idx)
        if l != 0:
            answer.append(l)

answer.sort()
print(len(answer))
for a in answer:
    print(a)