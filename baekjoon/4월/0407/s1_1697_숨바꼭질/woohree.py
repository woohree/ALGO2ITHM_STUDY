import sys
sys.stdin = open('L.txt')
from collections import deque


def bfs(start):
    news = deque()
    visited = [0] * 100001                  # 최댓값 기준으로 체크 리스트 작성
    news.append(start)
    time = 0

    while news:
        for _ in range(len(news)):
            now = news.popleft()
            if now == K:                    # 동생만나면 끝!
                return time
            visited[now] = 1
            ops = [now-1, now+1, 2*now]
            for op in ops:
                if 0 <= op <= 100000 and not visited[op]:
                    news.append(op)
        time += 1


N, K = map(int, input().split())
ans = bfs(N)
print(ans)
