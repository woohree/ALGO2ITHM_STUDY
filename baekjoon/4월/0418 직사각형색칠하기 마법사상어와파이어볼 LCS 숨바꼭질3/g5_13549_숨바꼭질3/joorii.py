from collections import deque
import sys
sys.stdin = open('M.txt')


# bfs
def find_and_seek():
    nexts = deque()
    nexts.append(N)
    visited[N] = 1

    while nexts:
        cur = nexts.popleft()

        if cur == K:        # 종료조건, 동생을 찾았을 떄
            return visited[cur] - 1

        moves = [cur * 2, cur - 1, cur + 1]     # 순서 중요
        for i in range(3):
            if 0 <= moves[i] < 100001 and not visited[moves[i]]:
                if i != 0:      # 순간이동이 아닐 떄, 1초 후
                    visited[moves[i]] = visited[cur] + 1
                elif i == 0:    # 순간이동일 때, 0초 후
                    visited[moves[i]] = visited[cur]
                nexts.append(moves[i])


# 수빈 위치 N, 동생 위치 K
N, K = map(int, input().split())
visited = [0 for _ in range(100001)]
print(find_and_seek())
