import sys
sys.stdin = open('L.txt')


# 숏코딩 + 효율 둘다 1위 ㅎ
def principal_period(chars):
    i = (chars + chars).find(chars, 1)      # 문자열 2번 더해서, 1번 인덱스부터 문자열 찾기(마지막 문자 위치)
    if i == -1:                             # 반복하지 않으면, n = 1
        return 1
    else:                                   # 반복한다면, n = 전체 길이를 i로 나눈 값
        return len(chars)//i


while 1:
    chars = sys.stdin.readline().rstrip()
    if chars == '.':
        break
    print(principal_period(chars))