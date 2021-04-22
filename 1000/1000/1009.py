a = int(input())
for i in range(0, a):
    b, c = map(int, input().split())
    res = pow(b, c, 10)
    print(10 if res == 0 else res)

# O(logN) 인데도 시간 초과....
# def d(base, exp):
#     if exp == 1:
#         return base
#     elif exp == 0:
#         return 1
#
#     if exp % 2 == 0:
#         res = d(base, exp // 2)
#         return res * res
#     else:
#         res = d(base, (exp - 1) // 2)
#         return res * res * base
#
# for i in range(0, a):
#     b, c = map(int, input().split())
#     res = d(b, c) % 10
#     print(10 if res == 0 else res)

# 이렇게 하면 c가 클 경우 연산량이 많아짐 O(N)
# for i in range(0, a):
#     b, c = map(int, input().split())
#     print(b ** c % 10)