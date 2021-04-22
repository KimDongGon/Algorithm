import math

a, b, c = map(int, input().split())
x = math.sqrt(a**2 / (1 + (b**2 / c**2)))
print(int(x * b / c) ,int(x))
