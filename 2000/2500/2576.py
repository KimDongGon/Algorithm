answer = []
for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        answer.append(n)

if not answer:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))