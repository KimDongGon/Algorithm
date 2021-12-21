n = int(input())

a = [int(i) for i in input().split()]

m = int(input())

b = [int(j) for j in input().split()]

a = dict.fromkeys(a, 1)

for _b in b:
    print(a.get(_b, 0))