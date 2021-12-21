def f(n, c):
    if n == 1 or c == 0:
        return 1
    return n * f(n - 1, c - 1)

n, c = map(int, input().split())
print(f(n, c) // f(c, c))