n = int(input())

switch = list(map(int, input().split()))

m = int(input())

for i in range(m):
    gender, no = map(int, input().split())

    if gender == 1:
        for j in range(no, n + 1, no):
            switch[j - 1] = 0 if switch[j - 1] == 1 else 1
    elif gender == 2:
        l = no - 2
        r = no
        while True:
            if 0 <= l and r <= n - 1 and switch[l] == switch[r]:
                l -= 1
                r += 1
            else:
                break
        for j in range(l + 1, r):
            switch[j] = 0 if switch[j] == 1 else 1

for i, s in enumerate(switch):
    if (i + 1) % 20 == 0:
        print(s)
    else:
        print(s, end=' ')

