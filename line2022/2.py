answer = 0

def solution(sentences, n):

    d = dict()

    for sentence in sentences:
        l = len(sentence)
        key = dict()
        for s in sentence:
            if s.isalpha():
                if s.isupper():
                    l += 1
                    key[s.lower()] = 1
                    key['shift'] = 1
                else:
                    key[s] = 1
        d[sentence] = [l, list(key.keys())]

    for i in range(len(sentences)):
        solve(i + 1, len(sentences), d[sentences[i]][1], n, d, d[sentences[i]][0], sentences)

    return answer

def solve(start, end, key, n, d, sum, sentences):
    global answer
    answer = max(answer, sum)

    if start == end:
        return

    for i in range(start, end):
        k = list(set(d[sentences[i]][1] + key))
        if len(k) <= n:
            solve(i + 1, end, k, n, d, sum+d[sentences[i]][0], sentences)

# print(solution(["line in line", "LINE", "in lion"], 5))
print(solution(["ABcD", "bdbc", "a", "Line neWs"], 7))