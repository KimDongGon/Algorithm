import heapq

def solution(req_id, req_info):
    answer = []
    buy = []
    sell = []
    cal = dict.fromkeys(set(req_id), [0, 0])

    # 최소 힙 우선순위 구매 가격, 먼저 들어온 순
    l = len(req_id)

    for i in range(l):
        TYPE, AMOUNT, PRICE = req_info[i]

        if TYPE == 1:
            heapq.heappush(buy, [-PRICE, i + 1, AMOUNT, req_id[i]])
        else:
            heapq.heappush(sell, [PRICE, i + 1, AMOUNT, req_id[i]])

    while buy and sell:
        # 가장 비싼거
        bT, bP, bA, bW = heapq.heappop(buy)
        # 가장 싼거
        sT, sP, sA, sW = heapq.heappop(sell)

        if -bT < sT:
            break
        if bA > sA:
            heapq.heappush(buy, [bT, l + 1, bA - sA, bW])
            cal[bW] = [cal[bW][0] + sA, cal[bW][1] - (sA * sT)]
            cal[sW] = [cal[sW][0] + sA, cal[sW][1] - (sA * sT)]

        elif bA < sA:
            heapq.heappush(sell, [sT, l + 1, sA - bA, sW])
            cal[bW] = [cal[bW][0] + bA, cal[bW][1] - (bA * (-bT))]
            cal[sW] = [cal[sW][0] + bA, cal[sW][1] - (bA * (-bT))]

    for k, v in cal.items():
        s = ""
        s += k
        if v[0] > 0:
            s += " +" + str(v[0])
        elif v[0] < 0:
            s += " -" + str(v[1])
        else:
            s += " " + "0"

        if v[0] > 0:
            s += " +" + str(v[0])
        elif v[0] < 0:
            s += " -" + str(v[1])
        else:
            s += " " + "0"
        answer.append(s)
    answer.sort()
    return answer

print(solution(["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"], [[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]))
# ["Andy +11 -240", "Louis 0 0", "Rohan -4 +100", "William -7 +140"]
print(solution(["Morgan", "Teo", "Covy", "Covy", "Felix"], [[0, 10, 50], [1, 35, 70], [0, 10, 30], [0, 10, 50], [1, 11, 40]]))
# ["Covy +1 -40", "Felix -11 +440", "Morgan +10 -400", "Teo 0 0"]