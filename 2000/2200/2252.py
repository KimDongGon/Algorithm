n, m = map(int, input().split())

arr = []

for _ in range(m):
    a, b = map(int, input().split())

    if a not in arr and b not in arr:
        arr.append(a)
        arr.append(b)
    elif a not in arr:
        arr.insert(arr.index(b), a)
        arr.append(b)