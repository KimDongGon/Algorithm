import sys

def nqueen(r):
    if r == n:
        global cnt
        cnt += 1
        return
    # for c in range(n):
    #     if visited[c]:
    #         continue

        # arr[r] = c
        # if check(r):
        #     visited[c] = True
        #     nqueen(r + 1)
        #     visited[c] = False

    for c in range(n):
        if not(visited[c] or visited2[r + c] or visited3[r - c + n - 1]):
            visited[c] = visited2[r + c] = visited3[r - c + n - 1] = True
            nqueen(r + 1)
            visited[c] = visited2[r + c] = visited3[r - c + n - 1] = False

# def check(r):
#     for i in range(r):
#         if r - arr[r] == i - arr[i] or r - arr[r] == i + arr[i]:
#             return False
#     return True

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    cnt = 0

    arr = [0] * n
    visited = [False] * n
    visited2 = [False] * (2*n - 1)
    visited3 = [False] * (2*n - 1)

    nqueen(0)
    print(cnt)

