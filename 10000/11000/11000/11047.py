n, k = map(int, input().split())

money = []

for _ in range(n):
    m = int(input())
    money.append(m)

i = len(money) - 1
answer = 0

while k > 0:
    if k // money[i] > 0:
        answer += k // money[i]
        k = k % money[i]
    else:
        i -= 1

print(answer)