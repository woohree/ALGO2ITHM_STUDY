from collections import deque
import sys
sys.stdin = open('G.txt')


def dfs(n):
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        
        # 현재 위치랑 목표위치가 같으면 몇 초 걸렸나 반환
        if x == k:
            return visited[x]
        
        # 이동 가능한 좌표
        moves = [x - 1, x + 1, x * 2]

        for move in moves:
            # 해당 범위를 넘어간 경우는 제외
            if 0 <= move <= 100000:
                if not visited[move]:
                    visited[move] = visited[x] + 1
                    queue.append(move)


n, k = map(int, input().split())

# 범위가 0부터 100000이기 때문
visited = [0 for _ in range(100000+1)]
answer = dfs(n)
print(answer)