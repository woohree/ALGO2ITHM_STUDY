# 5:25 시작
# N개의 옵션
# 각 옵션에 단축키를 의미하는 대표 알파벳을 지정하기
# 1. 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는지
#   만약 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정한다.
# 2. 만약 모든 단어의 첫 글자가 이미 지정이 되어있다면 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정
#   안 된 것이 있다면 단축키로 지정한다.
# 3. 어떠한 것도 단축키로 지정할 수 없다면 그냥 놔두며 대소문자를 구분치 않는다.
# 4. 위의 규칙을 첫 번째 옵션부터 N번째 옵션까지 차례대로 적용한다.

import sys
sys.stdin = open('B.txt')

N = int(input())
words = [input().split() for _ in range(N)]

short_cut = []
for word in words:
    check = 0
    for w in range(len(word)):
        if word[w][0].lower() not in short_cut:
            short_cut.append(word[w][0].lower())
            x = list(word[w])
            x.insert(1, ']')
            x.insert(0, '[')
            word[w] = ''.join(x)
            check += 1
            break
    if check == 0:
        for w in range(len(word)):
            for i in range(1, len(word[w])):
                if word[w][i].lower() not in short_cut:
                    short_cut.append(word[w][i].lower())
                    x = list(word[w])
                    x.insert(i+1, ']')
                    x.insert(i, '[')
                    word[w] = ''.join(x)
                    check += 1
                    break
            if check != 0:
                break

for n in range(N):
    print(*words[n])
