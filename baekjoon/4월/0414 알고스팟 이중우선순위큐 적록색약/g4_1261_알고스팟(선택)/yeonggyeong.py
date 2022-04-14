from collections import deque
import sys
sys.stdin = open('G.txt') 

def bfs():
    matrix = [list(input()) for _ in range(M)]
    visited = [[-1 for _ in range(N)] for _ in range(M)]

    queue = deque()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue.append((0,0))
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            new_x, new_y = x + dx[idx], y + dy[idx]
        
            if 0 <= new_x < M and 0 <= new_y < N and visited[new_x][new_y] == -1:
                # 벽이면 뚫고 가야하니깐 +1 해주기
                if int(matrix[new_x][new_y]):
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = visited[x][y] + 1
                
                # 벽이 아니면 뚫지 않아도 되기 때문에 visited[x][y] 값 그대로 가져가기
                # 벽은 최소한으로 뚫기 위해 벽이 아니면 가장 처음에 append
                else:
                    queue.appendleft((new_x, new_y))
                    visited[new_x][new_y] = visited[x][y]
    
    return visited




N, M = map(int, input().split())
answer = bfs()
print(answer[M-1][N-1])