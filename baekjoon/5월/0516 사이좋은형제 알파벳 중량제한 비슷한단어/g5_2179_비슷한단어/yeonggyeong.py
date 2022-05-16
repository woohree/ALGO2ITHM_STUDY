import sys
sys.stdin = open('G.txt')

N = int(sys.stdin.readline())

words = [(sys.stdin.readline().rstrip(), i) for i in range(N)]
# 정렬 ( 인접한 단어 찾기 )
words.sort()

max_prefix = ""
idx = 0
for j in range(N-1):
    word1, word2 = words[j], words[j+1]

    prefix = ""

    # 공통 접두사 찾기
    for k in range(min(len(word1[0]), len(word2[0]))):
        if word1[0][k] == word2[0][k]:
            prefix += word1[0][k]
        else:
            break
    # 최장 접두사이고 기존 idx보다 빠를때
    if len(prefix) > len(max_prefix) or len(prefix) == len(max_prefix) and min(word1[1], word2[1]) < idx:
        max_prefix = prefix
        idx = min(word1[1], word2[1])

answer = []
for word in words:
    if word[0][:len(max_prefix)] == max_prefix:
        answer.append(word)
answer.sort(key=lambda x: x[1])
print(answer[0][0])
print(answer[1][0])
