arr = []
call = [[False] * 5 for _ in range(5)]
answer = 0

for i in range(5):
    arr.append(list(map(int, input().split())))

def check():
    bingo = 0
    for idx in range(5):
        if idx == 0:
            count = 0
            for _idx in range(5):
                if call[_idx][_idx]:
                    count += 1
            if count == 5:
                bingo += 1
        elif idx == 4:
            count = 0
            for _idx in range(5):
                if call[4 - _idx][_idx]:
                    count += 1
            if count == 5:
                bingo += 1
        if call[idx].count(True) == 5:
            bingo += 1
    for idx in range(5):
        count = 0
        for _idx in range(5):
            if call[_idx][idx]:
                count += 1
        if count == 5:
            bingo += 1

    if bingo >= 3:
        return True
    return False

for i in range(5):
    for j in list(map(int, input().split())):
        for k in range(5):
            if j in arr[k]:
                call[k][arr[k].index(j)] = True
                break
        if check():
            break
        answer += 1

print(answer + 1)