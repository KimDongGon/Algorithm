def solution(money, costs):
    answer = 0

    arr = [1, 5, 10, 50, 100, 500]
    idx = 0
    d = {}

    for i, cost in enumerate(costs):
        d[arr[i]] = d.get(arr[i], 0) + cost

    arr = arr[::-1]

    while money != 0:
        m = 5001
        if idx > 5:
            break
        if money >= arr[idx]:
            for a in arr:
                if money >= a:
                    m = min(m, d[a] * (arr[idx] // a))
            answer += m
            money -= arr[idx]
        else:
            idx += 1
    return answer