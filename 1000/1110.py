import math
a = int(input())
b = math.floor(a / 10) + a % 10
c = (a % 10) * 10 + b % 10
cnt = 1
while True:
    if a == c:
        print(cnt)
        break
    else:
        cnt += 1
    b = math.floor(c / 10) + c % 10
    c = (c % 10) * 10 + b % 10
