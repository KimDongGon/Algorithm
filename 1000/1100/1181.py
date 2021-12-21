n = int(input())

words = []

for i in range(n):
    word = input()
    words.append(word)
words = list(set(words))
words = sorted(words)
words = sorted(words, key=len)

for word in words:
    print(word)