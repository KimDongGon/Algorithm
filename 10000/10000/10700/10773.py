k = int(input())
answer = []
for _ in range(k):
    _k = int(input())
    if _k == 0 and len(answer) > 0:
        answer.pop()
    else:
        answer.append(_k)

print(sum(answer))