import sys
a = int(sys.stdin.readline())
for i in range(0, a):
    c, d = map(int, sys.stdin.readline().split())
    print(c + d)