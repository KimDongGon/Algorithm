A, B = map(str, input().split())
answer = 0
sumA = 0
for a in A:
    sumA += int(a)

for b in B:
    answer += sumA * int(b)

# 시간 초과
# for a in A:
#     for b in B:
#         answer += int(a) * int(b)
print(answer)