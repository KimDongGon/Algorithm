n = int(input())

def solve(n):
    if n == 1:
        return ['*']
    arr = solve(n // 3)
    l = []
    for a in arr:
        l.append(a * 3)
    for a in arr:
        l.append(a + (' ' * (n // 3)) + a)
    for a in arr:
        l.append(a * 3)
    return l

print('\n'.join(solve(n)))