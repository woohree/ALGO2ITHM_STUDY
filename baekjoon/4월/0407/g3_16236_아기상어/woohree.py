import sys
from collections import deque
sys.stdin = open('L.txt')


def bfs(start):
    global fishes
    news = deque()
    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    news.append(start)
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    shark = 2                                       # 상어 크기
    eat = 0                                         # 먹은 물고기 수
    fish = deque()                                  # 동시간에 먹을 수 있는 물고기 좌표들
    time = total = 0                                # 시간

    while news:
        time += 1
        for _ in range(len(news)):
            now = news.popleft()
            for move in moves:
                new_r, new_c = now[0] + move[0], now[1] + move[1]
                if 0 <= new_r < N and 0 <= new_c < N and not visited[new_r][new_c] and mat[new_r][new_c] <= shark:
                    if 0 < mat[new_r][new_c] < shark:           # 먹을 수 있는 물고기 추가
                        fish.append((new_r, new_c))
                    news.append((new_r, new_c))
                    visited[now[0]][now[1]] = 1

        if fish:
            if len(fish) > 1:
                fish = [min(fish, key=lambda x: (x[0], x[1]))]  # 물고기 겹치면, 조건에 맞는거 고르기
            total += time
            time = 0
            mat[fish[0][0]][fish[0][1]] = 0                     # 물고기 제거
            news = deque()
            news.append(fish[0])                                # 먹은 물고기 자리로 이동
            visited = [[0]*N for _ in range(N)]                 # 방문 초기화
            visited[fish[0][0]][fish[0][1]] = 1
            fish = deque()                                      # 물고기 초기화
            eat += 1
            if eat == shark:                                    # 상어 레벨업
                shark += 1
                eat = 0
            fishes -= 1
            if not fishes:
                return total
    return total


N = int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
fishes = 0
for i in range(N):
    for j in range(N):
        if mat[i][j] == 9:
            start = (i, j)
            mat[i][j] = 0
        elif mat[i][j]:
            fishes += 1

if not fishes:
    print(0)
else:
    ans = bfs(start)
    print(ans)