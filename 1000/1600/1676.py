n = int(input())

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

s = str(fact(n))

answer = 0

for _s in s[::-1]:
    if _s != '0':
        break
    answer += 1

print(answer)