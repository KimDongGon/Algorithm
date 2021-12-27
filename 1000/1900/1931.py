import sys

n = int(input())
t = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    t.append([s, e])

t.sort(key=lambda x: (x[1], x[0]))

answer = 1
end = t[0][1]

for i in range(1, n):
    if t[i][0] >= end:
        end = t[i][1]
        answer += 1
print(answer)