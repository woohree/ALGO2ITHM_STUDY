'''
1. 입력 문자열은 소문자로 통일시킨다.
2. 알파벳인지 확인하면서 리스트에 저장한다.
3. 교집합과 합집합 수를 구한다.
4. answer 를 구한다.
'''


import math


def solution(str1, str2):
    # 1, 2번
    str1 = str1.lower()
    words1 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            words1.append(str1[i:i+2])

    str2 = str2.lower()
    words2 = []
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            words2.append(str2[i:i+2])

    # 3번
    g, h = 0, len(words1) + len(words2)
    for i in range(len(words1)):
        for j in range(len(words2)):
            if words1[i] == words2[j]:
                words2.pop(j)               # words2의 j번째 문자는 사용한 것이므로 pop시켜버린다.
                g += 1
                break
    h -= g                                  # 두 리스트 더한 값에서 교집합 수 빼면 합집합 수 완성!
    # 4번
    if h == 0:                              # 합집합 수가 0이라면 answer은 65536으로 통일
        answer = 65536
    else:
        answer = math.trunc(g / h * 65536)  # 소수점 버림
    return answer
