while True:
    sen = input()
    if sen == '#':
        break
    else:
        count = 0
        for alpha in sen:
            if alpha.lower() == 'a' or alpha.lower() == 'e' or alpha.lower() == 'i' or alpha.lower() == 'o' or alpha.lower() == 'u':
                count += 1
        print(count)