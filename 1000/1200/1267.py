num = int(input())

phone = list(map(int, input().split()))

M = []
Y = []
for i in phone:
    Y.append(10 * (i // 30 + 1))
    M.append(15 * (i // 60 + 1))

sumY = sum(Y)
sumM = sum(M)

if sumY > sumM:
    print('M', sumM)
elif sumY < sumM:
    print('Y', sumY)
else:
    print('Y', 'M', sumY)
