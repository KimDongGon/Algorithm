import sys

count = 0

while True:
    o, w = map(int, sys.stdin.readline().split())

    if o == 0 and w == 0:
        break

    while True:
        act, actNum = map(str, sys.stdin.readline().split())
        num = int(actNum)
        if act == '#' and num == 0:
            break
        elif w > 0:
            if act == 'F':
                w += num
            elif act == 'E':
                w -= num

    count += 1
    if o / 2 < w < o * 2:
        print(count, ':-)')
    elif w <= 0:
        print(count, 'RIP')
    else:
        print(count, ':-(')
