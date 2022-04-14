from collections import deque
import sys
sys.stdin = open('G.txt')

def bfs():
    queue = deque()
    queue.append(1)

    while queue:
        x = queue.popleft()
        visited[1] = 1
        
        # 위치가 100이면 함수 종료
        if x == 100:
            return

        for mv in range(1, 7):
            new_x = x + mv

            if new_x <= 100 and not visited[new_x]:
                # 사다리나 뱀이 있을 경우
                if matrix[new_x][1] in ['ladder', 'snake']:
                    new_x = matrix[new_x][2]
                if not visited[new_x]:
                    visited[new_x] = 1
                    counts[new_x] = counts[x] + 1
                    queue.append(new_x)

N, M = map(int, input().split())

matrix=[[i, '0', 0] for i in range(101)]
# 방문 여부 체크
visited = [0 for _ in range(101)]
# 위치 까지 걸린 시간 체크
counts = [0 for _ in range(101)]

# 사다리 담기
for _ in range(N):
    start, end = map(int, input().split())
    matrix[start][1] = 'ladder'
    matrix[start][2] = end

# 뱀 담기
for _ in range(M):
    start, end = map(int, input().split())
    matrix[start][1] = 'snake'
    matrix[start][2] = end

bfs()

print(counts[-1])

        