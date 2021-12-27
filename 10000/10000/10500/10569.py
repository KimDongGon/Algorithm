t = int(input())

answer = []

for _ in range(t):
    v, e = map(int, input().split())
    answer.append(2 - v + e)

for a in answer:
    print(a)