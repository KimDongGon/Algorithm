def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


J = int(input())
if J < 4:
    print(0)
else:
    print(int(factorial(J - 1) / (factorial(J - 4) * factorial(3))))
