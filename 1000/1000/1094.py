X = int(input())

stick = 64
answer = 0

while stick != 0:
    if stick > X:
        stick /= 2
    else:
        answer += 1
        X -= stick

print(answer)