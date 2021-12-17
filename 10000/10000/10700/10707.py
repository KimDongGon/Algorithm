A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = A * P
Y = B + (D * (P - C) if C < P else 0)
if X > Y:
    print(Y)
else:
    print(X)