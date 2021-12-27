m = int(input())
n = int(input())

_m = int(m ** (1 / 2))
_n = int(n ** (1 / 2))

r = [x ** 2 for x in range(_m, _n + 1)]
answer = [_r for _r in r if _r in range(m, n + 1)]
    
if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))