# N진법 함수 변환(재귀함수)
def convert(num, base):
    tmp = '0123456789ABCDEF'
    # divmod = 몫과 나머지를 튜플 형태로 반환
    q, r = divmod(num, base)
    # 몫이 0이면 나머지를 반환함
    if q == 0:
        # tmp의 r번째를 반환
        return tmp[r]
    # 몫이 0이 아니라면 한번 더 실행함
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    answer = ''
    test = ''
    # m*t가 최대로 구해야 하는 숫자의 갯수임(그리고 자릿수 풀어 쓴 것 test에 추가함)
    for i in range(m * t):
        test += str(convert(i, n))
    # test에서 p번 순서마다 골라옴
    while len(answer) < t:
        answer += test[p - 1]
        p += m

    return answer