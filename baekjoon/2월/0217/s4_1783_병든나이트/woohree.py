import sys
sys.stdin = open('L.txt')

# 40분

def get_route_of_cursed_knight(N, M):
    route = 0
    # 이동 조건을 모두 한번씩 사용한 범위
    # 첫 위치 + 이동 조건 네번 + 남은 거리(위아래로 두칸씩 움직이면서 우측으로 한칸씩)
    if N > 2 and M > 6:
        route = 5 + (M - 7)
    # 위아래로 두칸씩 움직이면서 우측으로 한칸씩
    # 그렇지만 5이상 이동하려면 이동 조건을 모두 사용해야 하므로 최대가 4
    elif N > 2:
        if M < 5:
            route = M
        elif 4 < M < 7:
            route = 4
    # 위아래로 한칸씩 움직이면서 우측으로 두칸씩
    # 우측으로 두칸이라 수가 적음 (최대 4)
    elif N == 2:
        if M < 5:
            route = (M+1) // 2
        elif 4 < M < 7:
            route = 3
        elif M > 6:
            route = 4
    # 세로가 1이면 그냥 1임
    elif N == 1:
        route = 1

    return route

data = list(map(int, input().split()))
N, M = data[0], data[1]
ans = get_route_of_cursed_knight(N, M)
print(ans)