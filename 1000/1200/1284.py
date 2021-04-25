while True:
    a = input()
    if int(a) == 0:
        break
    sum = len(a) + 1
    for i in a:
        if int(i) == 1:
            sum += 2
        elif int(i) == 0:
            sum += 4
        else:
            sum += 3
    print(sum)
