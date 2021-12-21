while True:
    num = [int(x) for x in input().split()]
    if not any(num):
        break
    num.sort()
    if num[0] ** 2 + num[1] ** 2 == num[2] ** 2:
        print('right')
    else:
        print('wrong')