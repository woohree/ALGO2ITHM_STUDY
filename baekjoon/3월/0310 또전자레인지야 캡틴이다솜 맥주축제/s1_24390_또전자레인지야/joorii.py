import sys
sys.stdin = open('M.txt')

def shortest_count(m, s):
    # 10초, 1분, 10분, 조리시작(30초)
    cnt = [0, 0, 0, 0]

    # 분 단위 계산하기
    if m // 10:
        cnt[2] = m // 10
        m = m % 10
    cnt[1] = m

    # 초 단위 계산하기
    if s // 30:
        cnt[3] = s // 30
        s = s % 30
    cnt[0] = s // 10

    result = 0
    for i in range(len(cnt)):
        # 조리시작 버튼이 추가적으로 눌려져야 될 때
        if i == 3 and cnt[i] == 0:
            result += cnt[i] + 1
        result += cnt[i]

    return result


M, S = map(int, input().split(':'))

print(shortest_count(M, S))
