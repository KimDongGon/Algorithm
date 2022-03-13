import math


def solution(n, edges):
    answer = 0
    d = {}

    for edge in edges:
        d[edge[0]] = d.get(edge[0], []) + [edge[1]]
        d[edge[1]] = d.get(edge[1], []) + [edge[0]]

    def solve(cur, visited):
        nonlocal answer
        l = len(visited)
        if l == 3:
            answer += 1
        if l > 3:
            answer += (math.factorial(l - 1) // (math.factorial(l - 1 - 2) * math.factorial(2))) - 1
        for v in d[cur]:
            if v not in visited:
                solve(v, visited + [v])

    for i in range(n):
        solve(i, [i])

    return answer