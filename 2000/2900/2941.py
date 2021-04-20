arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
cnt = len(a)
for i in arr:
    cnt -= a.count(i)
print(cnt)
