a = int(input())


def d(num):
    if num[0] - num[1] == num[1] - num[2]:
        return True
    return False


if a < 100:
    print(a)
else:
    cnt = 99
    for i in range(100, a + 1):
        b = [int(j) for j in str(i)]
        if d(b):
            cnt += 1
    print(cnt)