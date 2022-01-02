n = int(input())

answer = []

for _ in range(n):
    r, e, c = map(int, input().split())
    if e - c > r:
        answer.append('advertise')
    elif e - c == r:
        answer.append('does not matter')
    else:
        answer.append('do not advertise')

for a in answer:
    print(a)