from collections import deque
import sys
sys.stdin = open('G.txt')

N, M = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(N)]

graph = [[] for _ in range(N*M)]
villages = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for row in range(N):
    for col in range(M):

        if matrix[row][col] == 1:
            villages.append([row, col])

        for i in range(4):
            new_x, new_y = row+dx[i], col + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M:
                graph[row*N + col].append(new_x * N + new_y)



def bfs(start):

    visited = [False for _ in range(N*M)]
    for village in villages:
        visited[village[0]*N + village[1]] = True

    addiction = 0
    queue = deque()
 
    if visited[start] == True:
        addiction += 1

    visited[start] = 'control'

    if graph[start]:
        for next in graph[start]:
            if visited[next] != 'control':
                queue.append(next)
    
    time = 0

    while queue: 
        len_q = len(queue)

        if addiction == len(villages):
                return time

        time += 1

        for i in range(len_q):
            now = queue.popleft()

            if visited[now] == True:
                addiction += 1
            
            visited[now] = 'control'

            for next in graph[now]:
                if visited[next] != 'control':
                    queue.append(next)
                

print(bfs(16))