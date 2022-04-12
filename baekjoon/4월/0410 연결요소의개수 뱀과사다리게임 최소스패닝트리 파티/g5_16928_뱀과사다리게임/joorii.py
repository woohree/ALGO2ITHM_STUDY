from collections import deque
import sys
sys.stdin = open('M.txt')


# bfs
def game():
    # [현재 위치, 이동 횟수]
    nexts = deque([[1, 0]])
    visited[1] = 1
    while nexts:
        cur = nexts.popleft()
        if cur[0] == 100:                               # 종료조건
            return cur[1]
        for c in range(1, 7):                           # 1 ~ 6 까지의 경우 탐색
            nxt, cnt = cur[0] + c, cur[1] + 1
            if 1 <= nxt < 101 and not visited[nxt]:
                if nxt in ladders:                      # 다음 칸에 사다리가 있을 떄
                    nexts.append([ladders[nxt], cnt])
                    visited[ladders[nxt]] = 1
                elif nxt in snakes:                     # 다음 칸에 뱀이 있을 때
                    nexts.append([snakes[nxt], cnt])
                    visited[snakes[nxt]] = 1
                else:
                    nexts.append([nxt, cnt])
                    visited[nxt] = 1


# 사다리의 수 N, 뱀의 수 M
N, M = map(int, sys.stdin.readline().split())
ladders = dict(map(int, sys.stdin.readline().split()) for _ in range(N))
snakes = dict(map(int, sys.stdin.readline().split()) for _ in range(M))
visited = [0 for _ in range(101)]

print(game())
