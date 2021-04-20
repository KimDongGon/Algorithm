a, b = input().split()
revA = int(a[2] + a[1] + a[0])
revB = int(b[2] + b[1] + b[0])
if revA > revB:
    print(revA)
else:
    print(revB)