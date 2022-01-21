n = int(input())
d = dict()
num = list(map(int, input().split()))
for n in num:
    d[n] = d.get(n, 0) + 1

m = int(input())
answer = []
num = list(map(int, input().split()))
for n in num:
    answer.append(d.get(n, 0))

print(' '.join(map(str, answer)))