import heapq

def solution(arr, brr):
    answer = 0
    # 큰 값을 기준으로 왼쪽과 오른쪽에 필요한만큼 나눠줌
    hq = []

    for i, a in enumerate(arr):
        heapq.heappush(hq, [-a, a, i])

    print(hq)

    return answer

print(solution([3, 7, 2, 4], [4, 5, 5, 2]))
print(solution([6, 2, 2, 6], [4, 4, 4, 4]))
print(solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3])) # 4
print(solution([1, 3, 5, 4, 2], [3, 3, 3, 3, 3])) # 4