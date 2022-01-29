import sys

n, m = map(int, sys.stdin.readline().split())
d = dict()
visited = [False] * (n + 1)
answer = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    d[u] = d.get(u, []) + [v]
    d[v] = d.get(v, []) + [u]

for k, v in d.items():
    if not visited[k]:
        visited[k] = True
        answer += 1
    for _v in v:
        if not visited[_v]:
            visited[_v] = True

print(answer + len([x for x in visited if not x]) - 1)
