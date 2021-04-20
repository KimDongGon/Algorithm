a = input().strip().split(' ')
cnt = 0
for i in a:
    if i.replace(" ", "") != "":
        cnt += 1
print(cnt)