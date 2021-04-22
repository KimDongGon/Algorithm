a, b = map(int, input().split())
x = (a + b) // 2
y = (a - b) // 2
if x + y != a or x - y != b:
    print(-1)
else:
    if x >= 0 and y >= 0:
        print(x, y)
    else:
        print(-1)