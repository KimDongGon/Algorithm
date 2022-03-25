arr = list(map(int, input().split()))

visited = [False] * 4

MIN = 100000001


def comb(cnt, start):
    if cnt == 2:
        global MIN
        teamA = 0
        teamB = 0
        for i, v in enumerate(visited):
            if v:
                teamA += arr[i]
            else:
                teamB += arr[i]
        MIN = min(MIN, abs(teamA - teamB))
        return

    for i in range(start, 4):
        if visited[i]: continue
        visited[i] = True
        comb(cnt + 1, i + 1)
        visited[i] = False


comb(0, 0)

print(MIN)
