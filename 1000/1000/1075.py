N = int(input())
F = int(input())
N = N - (N % 100)

while N % F != 0:
    N += 1

print(str(N)[len(str(N)) - 2:])