M = int(input())
position = 1
for _ in range(M):
    X, Y = map(int, input().split())
    if X == position:
        position = Y
    elif Y == position:
        position = X
print(position)