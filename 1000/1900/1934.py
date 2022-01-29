T = int(input())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(T):
    a, b = map(int, input().split())
    if a > b:
        print(a * b // gcd(a, b))
    else:
        print(a * b // gcd(b, a))