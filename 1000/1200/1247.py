import sys
arr = []
for _ in range(0, 3):
    N = int(input())
    num = list(int(sys.stdin.readline()) for __ in range(N))
    S = 0
    for i in num:
        S += i
    arr.append(S)

for S in arr:
    if S > 0:
        print('+')
    elif S < 0:
        print('-')
    else:
        print('0')

