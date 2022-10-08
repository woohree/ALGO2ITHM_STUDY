import sys
sys.stdin = open('L.txt')


def find_IOI(S):
    IOI = 'IO'*N + 'I'                      # 찾을 문자열
    cnt = 0

    if IOI not in S:                        # 없으면 그냥 바로 0 반환!
        return cnt

    while IOI in S:                         # S 안에 IOI가 있다면,
        cnt += 1                            # 하나 추가!
        i = S.index(IOI) + len(IOI)         # 새로운 인덱스(i) 찾은 문자열의 종료지점 바로 다음 인덱스
        len_S = len(S)

        for j in range(i, len_S, 2):
            if j >= len_S - 1:              # 인덱스 에러 방지
                break
            elif S[j] + S[j+1] == 'OI':     # 문자열 찾았는데, 그 뒤에 바로 OI가 붙으면 하나 추가!
                cnt += 1
                i += 2                      # 새로운 인덱스도 2칸 뒤로 밀기!
            else:                           # OI가 안나오면 탈출!
                break

        S = S[i:]                           # S를 새로운 인덱스부터 슬라이싱!

    return cnt


N = int(input())
M = int(input())
S = input()
ans = find_IOI(S)
print(ans)
