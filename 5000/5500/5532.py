a = list(int(input()) for _ in range(5))
korea = a[2] // a[4] + (1 if a[2] % a[4] != 0 else 0)
math = a[1] // a[3] + (1 if a[1] % a[3] != 0 else 0)
print(a[0] - (korea if korea > math else math))