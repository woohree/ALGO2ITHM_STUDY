import sys
sys.stdin = open('L.txt')

# 10분


def is_group_word(word):
    # 중복된 문자가 나중에 다시 나오는 지 판별할 temp
    # 한번 나온 문자가 나중에 다시 나오면(연속은 상관없음) 그룹 단어가 아님!
    length = len(word)
    temp = []

    for idx in range(length - 1):
        # 중복 문자가 다시 나오면 탈출!
        if word[idx] in temp:
            return 0
        
        else:
            # 다음 문자와 비교해 다른 경우, temp에 현 문자 추가!
            if word[idx] != word[idx+1]:
                temp.append(word[idx])

                # 마지막 문자 검사
                if idx == length - 2:
                    if word[idx+1] in temp:
                        return 0

    return 1


T = int(input())
ans = 0

for tc in range(T):
    word = input()
    ans += is_group_word(word)

print(ans)
