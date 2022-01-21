n = int(input())
num = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_value = -1000000001
min_value = 1000000001

def solve(k, x):
    if k == n - 1:
        global max_value
        global min_value
        max_value = max(max_value, x)
        min_value = min(min_value, x)

    for i in range(len(ops)):
        if ops[i] > 0:
            ops[i] -= 1
            if i == 0:
                solve(k + 1, x + num[k + 1])
            elif i == 1:
                solve(k + 1, x - num[k + 1])
            elif i == 2:
                solve(k + 1, x * num[k + 1])
            elif i == 3:
                if x < 0:
                    solve(k + 1, -(-x // num[k + 1]))
                else:
                    solve(k + 1, x // num[k + 1])
            ops[i] += 1

solve(0, num[0])

print(max_value)
print(min_value)

# from itertools import permutations as p
#
# n = int(input())
# op = ['+', '-', '*', '//']
# num = list(map(int, input().split()))
# max_value = -1000000001
# min_value = 1000000001
# ops = []
#
# for i, o in enumerate(list(map(int, input().split()))):
#     if o != 0:
#         ops.extend([op[i]] * o)
# for _p in p(ops, n - 1):
#     s = num[0]
#     for i, __p in enumerate(_p):
#         if __p == '+':
#             s += num[i + 1]
#         elif __p == '-':
#             s -= num[i + 1]
#         elif __p == '*':
#             s *= num[i + 1]
#         elif __p == '//':
#             if s < 0:
#                 s = -(-s // num[i + 1])
#             else:
#                 s //= num[i + 1]
#
#     max_value = max(max_value, s)
#     min_value = min(min_value, s)
#
# print(max_value)
# print(min_value)