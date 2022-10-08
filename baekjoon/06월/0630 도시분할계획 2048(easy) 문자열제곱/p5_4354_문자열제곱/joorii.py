import sys
sys.stdin = open('M.txt')


def square():
    ltc = len(tc)
    pi = [0] * ltc      # 탐색할 문자열의 접두사, 접미사 길이를 저장
    j = 0       # 접두사
    for i in range(1, ltc):     # 접미사
        if j > 0 and tc[i] != tc[j]:
            j = pi[j - 1]
        if tc[i] == tc[j]:
            pi[i] = j + 1
            j += 1

    rep = ltc - pi[-1]    # 반복되는 문자열의 크기
    if ltc % rep != 0:
        print(1)
    else:
        print(ltc // rep)


while 1:
    tc = sys.stdin.readline().rstrip()
    if tc == '.':       # 종료조건
        break
    square()
