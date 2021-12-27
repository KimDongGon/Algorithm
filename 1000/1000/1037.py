n = int(input())
if n == 1:
    k = int(input())
    print(k ** 2)
elif n == 2:
    a, b = map(int, input().split())
    print(a * b)
else:
    answer = list(map(int, input().split()))
    answer.sort()
    print(answer[0] * answer[-1])