import sys
from collections import deque
sys.stdin = open('L.txt')


def bfs(start):
    visited[start] = 1
    news = deque()
    news.append(start)
    cnt = 0

    while news:
        for _ in range(len(news)):
            now = news.popleft()
            if now == 100:                              # 100도착하면 끝!
                return cnt
            for move in range(1, 7):                    # 주사위 1 ~ 6
                new = now + move
                if new <= 100 and not visited[new]:
                    visited[new] = 1
                    if game.get(new):                   # 사다리 혹은 뱀이 있는 칸이면,
                        new = game.get(new)             # 그 위치로 이동
                    news.append(new)
        cnt += 1


N, M = map(int, sys.stdin.readline().rstrip().split())
game = {}
visited = [0] * 101
for _ in range(N+M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    game[x] = y
ans = bfs(1)
print(ans)
