import itertools
a = int(input())
cnt = a
for i in range(0, a):
    b = input()
    c = ''.join(i for i, _ in itertools.groupby(b))
    d = [l for l in itertools.groupby(b)]
    # d = itertools.groupby(b)
    print(d)
    for j in c:
        if c.count(j) > 1:
            index = c.index(j)
            if index == 0:
                if c[index] != c[index + 1]:
                    cnt -= 1
                    break
            elif index == len(c) - 1:
                if c[index] != c[index - 1]:
                    cnt -= 1
                    break
            else:
                if c[index] != c[index - 1] and c[index] != c[index + 1]:
                    cnt -= 1
                    break
print(cnt)