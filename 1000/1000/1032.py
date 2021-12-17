N = int(input())
file = list(input() for _ in range(N))
answer = ""
if N > 1:
    for i in range(len(file[0])):
        string = (file[0])[i]
        for j in range(1, len(file)):
            if (file[j])[i] != string:
                answer += '?'
                break
            else:
                if j == len(file) - 1:
                    answer += string
    print(answer)
else:
    print(file[0])