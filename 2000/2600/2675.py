a = int(input())
for i in range(0, a):
    b, c = input().split()
    for j in range(0, len(c)):
        print(c[j] * int(b), end='')
    print()