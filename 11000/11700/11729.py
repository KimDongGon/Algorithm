n = int(input())

answer = []

def hanoi(n, x, y, z):
    if n == 1:
        answer.append([x, z])
    else:
        hanoi(n - 1, x, z, y)
        answer.append([x, z])
        hanoi(n - 1, y, x, z)

hanoi(n, 1, 2, 3)
print(len(answer))
for a in answer:
    print(' '.join(map(str, a)))