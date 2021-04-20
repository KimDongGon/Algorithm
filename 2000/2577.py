a = int(input())
b = int(input())
c = int(input())
length = len(str(a * b * c))
for i in range(0, 10):
    num = a * b * c
    cnt = 0
    for j in range(0, length):
        if num % 10 == i:
            cnt += 1
        num = num // 10
    print(cnt)