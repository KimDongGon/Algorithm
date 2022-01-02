t = int(input())

d = [-1, 0, 1]

for _ in range(t):
    x, y = map(int, input().split())
    temp = (y - x) ** (1 / 2)
    if round(temp) == temp:
        print(2 * round(temp) - 1)
    elif round(temp) == int(temp):
        print(int(temp) * 2)
    else:
        print(int(temp) * 2 + 1)