a = int(input())
for i in range(0, a):
    string = input()
    sum = 0
    score = 0
    for j in range(0, len(string)):
        if string[j] == 'O':
            score += 1
            sum = sum + score
        else:
            score = 0
    print(sum)