# 1:55 시작 => 2:25 완료... 30분 소요
# 그룹단어: 단어에 존재하는 모든 문자에 대해서 각 문자가 연속해서 나타나는 경우
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력
# N은 100보다 작거나 같은 자연수

# 'aba abab abcabc a'에서 앞에 세 단어들은 앞서 나왔던 문자가 뒤에서 다시 나오기때문에
# 그룹단어가 아니고, 오직 a만이 그룹단어로 인정된다.

import sys
sys.stdin = open('B.txt')

N = int(input())
words = [input() for _ in range(N)]

# 그룹단어가 아닌 것의 개수 찾기
not_group_word = 0
for word in words:
    group_word = [word[0]]
    for i in range(1, len(word)):
        # 이전 문자가 지금 문자와 다르다면,
        if word[i] != word[i - 1]:

            # 문자가 group_word 리스트에 있으면 카운팅하고 braek로 for문 빠져나가서 다음 단어 검사
            if word[i] in group_word:
                not_group_word += 1
                break

            # 뒤에서 중복 안되면 group_word 리스트에 추가
            else:
                group_word.append(word[i])

# 출력은 전체 단어 개수에서 그룹단어가 아닌 것을 빼서 계산
print(N - not_group_word)
