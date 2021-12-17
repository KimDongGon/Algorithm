n = int(input())
for i in range(2 * n - 1):
    l = n - 1 - abs(n - i - 1)
    print(' ' * l + '*' * (2 * n - 1 - 2 * l))