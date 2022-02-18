width, height = map(int, input().split())
n = int(input())
shop = []
answer = 0

for i in range(n + 1):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        arr = [0, arr[1]]
    elif arr[0] == 2:
        arr = [height, arr[1]]
    elif arr[0] == 3:
        arr = [arr[1], 0]
    elif arr[0] == 4:
        arr = [arr[1], width]

    if i == n:
        dong = arr
    else:
        shop.append(arr)

for a in shop:
    # 행이 같은 경우
    if a[0] == dong[0]:
        # 행이 양쪽 끝에 없는 경우 -> 방향이 정 반대
        if a[0] != 0 and a[0] != height:
            answer += width + min(abs(a[0] + dong[0]), abs(height - a[0] + height - dong[0]))
        else:
            answer += abs(a[1] - dong[1])
    # 열이 같은 경우
    elif a[1] == dong[1]:
        if a[1] != 0 and a[1] != width:
            answer += height + min(abs(a[1] + dong[1]), abs(width - a[1] + width - dong[1]))
        else:
            answer += abs(a[0] - dong[0])
    # 행과 열이 다른 경우
    else:
        # 행의 차이가 높이와 같은 경우 -> 각각 남과 북
        if abs(a[0] - dong[0]) == height:
            answer += height + min(abs(a[1] + dong[1]), abs(width - a[1] + width - dong[1]))
        # 열의 차이가 넓이와 같은 경우 -> 각각 동과 서
        elif abs(a[1] - dong[1]) == width:
            answer += width + min(abs(a[0] + dong[0]), abs(height - a[0] + height - dong[0]))
        else:
            answer += abs(a[0] - dong[0]) + abs(a[1] - dong[1])

print(answer)