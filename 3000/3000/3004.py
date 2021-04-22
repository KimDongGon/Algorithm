a = int(input())
if a % 2 == 0:
    print((2 + (a // 2 - 1)) ** 2)
else:
    print((2 + a // 2) * (1 + a // 2))

# row = int(n / 2)
# col = n - row
# result = (row + 1) * (col + 1)