m = [300, 60, 10]
t = int(input())

answer = [0] * 3

for i, _m in enumerate(m):
    if t // _m != 0:
        answer[i] = t // _m
        t = t % _m

if t > 0:
    print(-1)
else:
    print(' '.join(map(str, answer)))