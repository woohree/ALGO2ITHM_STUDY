from collections import deque
import sys
sys.stdin = open('G.txt')


def bfs(N, K):
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()

        if x == K:
            return visited[x]
        
        moves = [2*x, x-1, x+1]

        for move in moves:
            if 0 <= move <= 100000 and not visited[move]:
                # 순간이동이라서 시간 추가 x
                if move == 2*x:
                    visited[move] = visited[x]
                else:
                    visited[move] = visited[x] + 1
                queue.append(move)
    return -1

N, K = map(int, input().split())

visited = [0 for _ in range(1000001)]
answer = bfs(N, K)
print(answer)
            

    
