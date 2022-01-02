notSelf = []


def d(num):
    return num + sum([int(i) for i in str(num)])


for i in range(1, 10001):
    number = d(i)
    if number <= 10000:
        notSelf.append(number)

for i in range(1, 10001):
    if i not in notSelf:
        print(i)