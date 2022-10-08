import sys
sys.stdin = open('M.txt')


def knight_road(N, M):
    if N == 1:
        return 1
    elif N == 2:
        # 세로 길이가 2일 때 이동 횟수가 4보다 작은 경우
        if M < 9:
            return (M + 1) // 2
        # 세로 길이가 2일 때 최대 이동 횟수
        else:
            return 4
    elif N >= 3:
        if M >= 7:
            return M-2
        # 세로 길이가 3 이상일 떄 이동 횟수가 4보다 적을 때
        else:
            if M < 5:
                return M
            else:
                return 4


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    print(knight_road(N, M))




