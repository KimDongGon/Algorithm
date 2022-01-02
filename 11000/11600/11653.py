n = int(input())

answer = []
for i in range(2, int(n ** (1 / 2)) + 1):
    while n % i == 0:
        n //= i
        answer.append(i)

for a in answer:
    print(a)

if n != 1:
    print(n)