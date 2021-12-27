import sys

s = set()
a = set([str(x) for x in range(1, 21)])

m = int(input())

for _ in range(m):
    c = sys.stdin.readline().split()
    if c[0] == 'add':
        s.add(c[1])
    elif c[0] == 'remove':
        if c[1] in s:
            s.remove(c[1])
    elif c[0] == 'check':
        if c[1] in s:
            print(1)
        else:
            print(0)
    elif c[0] == 'toggle':
        if c[1] in s:
            s.remove(c[1])
        else:
            s.add(c[1])
    elif c[0] == 'all':
        s = a
    elif c[0] == 'empty':
        s = set()