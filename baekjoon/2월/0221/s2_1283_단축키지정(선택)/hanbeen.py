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
for i in range(N):
    answer = []
    count = 0
    for j in range(len(words[i])):
        if words[i][j][0] not in short_cut:
            short_cut.append(words[i][j][0].upper())
            short_cut.append(words[i][j][0].lower())
            answer.append(words[i][j].replace(words[i][j][0], '[' + words[i][j][0] + ']'))

            if len(words[i]) > 1 and count == 0:
                for k in range(1, len(words[i])):
                    answer.append(words[i][k])
            break
        else:
            count += 1
            answer.append(words[i][j])
    if count < len(words[i]):
        answer = ' '.join(answer)
        print(answer)

    if count == len(words[i]):
        for j in range(len(words[i])):  # 0~1
            answer = []
            count = end = 0
            for m in range(len(words[i][j])):
                if words[i][j][m] not in short_cut:
                    short_cut.append(words[i][j][m].upper())
                    short_cut.append(words[i][j][m].lower())
                    answer.append(words[i][j].replace(words[i][j][m], '[' + words[i][j][m] + ']'))
                    if len(words[i]) > 1 and count == 0:
                        for k in range(1, len(words[i])):
                            answer.append(words[i][k])
                    end = 1
                    break
            if end != 0:
                answer = ' '.join(answer)
            else:
                break
            print(answer)
