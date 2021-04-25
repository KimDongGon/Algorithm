N, L, D = map(int, input().split())
maxT = (N * (L + 5)) - 5
startT = L
endT = L + 5
now = D
check = False
while now < maxT:
    if startT <= now <= endT - 1:
        print(now)
        check = True
        break
    else:
        if now < startT:
            now += D
        else:
            startT = endT + L
            endT = startT + 5

if not check:
    print(now)
# check = False
# for i in range(1, N + 1):
#     startT = endT + L
#     endT += L + 5
#     while ring < endT:
#         ring += D
#         if startT <= ring <= endT - 1:
#             check = True
#             print(ring)
#             break
#     if check:
#         break
