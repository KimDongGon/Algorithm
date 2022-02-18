n = int(input())
answer = []
num = list(map(int, input().split()))

for i in range(n):
    if num[i] != 0:
        answer.insert(i - num[i], i + 1)
    else:
        answer.append(i + 1)

print(' '.join(map(str, answer)))