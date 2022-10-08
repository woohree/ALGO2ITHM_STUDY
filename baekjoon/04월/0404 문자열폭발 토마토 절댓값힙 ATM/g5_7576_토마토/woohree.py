import sys
from collections import deque
sys.stdin = open('L.txt')


def bfs(news):
    global ripes
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    days = 0

    while news:
        days += 1
        for _ in range(len(news)):
            now = news.popleft()
            for move in moves:
                new_r, new_c = now[0] + move[0], now[1] + move[1]
                if 0 <= new_r < N and 0 <= new_c < M and not tomatos[new_r][new_c]:
                    news.append((new_r, new_c))
                    tomatos[new_r][new_c] = 1
                    ripes += 1

        if ripes == complete:                       # 현재 날짜까지, 익은 토마토 수가 전체 토마토와 같다면,
            return days                             # 날짜 반환

    return -1                                       # 익을 거 다 익었는데 전체 토마토 수보다 작다면, -1 반환(다 못 익힘)


M, N = map(int, sys.stdin.readline().split())
tomatos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
news = deque()
ripes = blanks = 0

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            news.append((i, j))
            ripes += 1                              # 익은 토마토
        elif tomatos[i][j] == -1:
            blanks += 1                             # 빈 공간

complete = N * M - blanks                           # 종료 조건, 토마토 갯수
if ripes == complete:
    print(0)
elif not news:
    print(-1)
else:
    ans = bfs(news)
    print(ans)