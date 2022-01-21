n = int(input())
num = 665
for i in range(0, n):
    while True:
        num += 1
        if str(num).count('666') >= 1:
            break
print(num)