n = input()
answer = 0
for i, _n in enumerate(n):
    if i == 0:
        answer += 10
    else:
        if _n == n[i - 1]:
            answer += 5
        else:
            answer += 10

print(answer)