a, b = map(int, input().split())
answer = min(((a - a // 2) - a // 2) * b, ((b - b // 2) - b // 2) * a)
print(answer)