import sys
sys.stdin = open('B.txt')

'''
1. 보자마자 dfs 생각나던데 dp를 떠올리려면 어떻게 하나 싶다.(9% 시간초과)
2. 
'''

sentence = list(sys.stdin.readline().rstrip())
L = len(sentence)
N = int(sys.stdin.readline().rstrip())
words = [[] for _ in range(51)]
for _ in range(N):
    word = list(sys.stdin.readline().rstrip())
    if L >= len(word):
        words[len(word)].append(word)

'''
def dfs(start, ans):
    global answer
    if start == L:
        if answer > ans:
            answer = ans
        return

    for i in range(start, L):
        if words[i - start + 1]:
            for w in words[i - start + 1]:
                word1 = sentence[start:i+1]
                word2 = w
                if sorted(word1) == sorted(word2):
                    count = 0
                    for j in range(i - start + 1):
                        a = w[j]
                        b = sentence[j+start]
                        if w[j] != sentence[j + start]:
                            count += 1
                    dfs(i+1, ans + count)
    return


sentence = list(sys.stdin.readline().rstrip())
L = len(sentence)
N = int(sys.stdin.readline().rstrip())
words = [[] for _ in range(51)]
for _ in range(N):
    word = list(sys.stdin.readline().rstrip())
    if L >= len(word):
        words[len(word)].append(word)
answer = 51
dfs(0, 0)
if answer == 51:
    print(-1)
else:
    print(answer)
'''
