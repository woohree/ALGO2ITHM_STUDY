import sys
sys.stdin = open('L.txt')

# 40분

def get_route_of_cursed_knight(N, M):
    route = 0
    if N > 2 and M > 6:
        route = 5 + (M - 7)
    elif N > 2:
        if M < 5:
            route = M
        elif 4 < M < 7:
            route = 4
    elif N == 2:
        if M < 5:
            route = (M+1) // 2
        elif 4 < M < 7:
            route = 3
        elif M > 6:
            route = 4
    elif N == 1:
        route = 1

    return route

data = list(map(int, input().split()))
N, M = data[0], data[1]
ans = get_route_of_cursed_knight(N, M)
print(ans)