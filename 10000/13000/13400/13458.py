n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for _a in a:
    if _a - b > 0:
        answer += (_a - b) // c + (2 if (_a - b) % c != 0 else 1)
    else:
        answer += 1

print(answer)