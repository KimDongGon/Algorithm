w, h = map(int, input().split())

p, q = map(int, input().split())

t = int(input())

p = p + t % (w * 2)
q = q + t % (h * 2)

if p > w:
    _p = 2 * w - p
    if _p >= 0:
        p = _p
    else:
        p = -_p

if q > h:
    _q = 2 * h - q
    if _q >= 0:
        q = _q
    else:
        q = -_q

print(p, q)
