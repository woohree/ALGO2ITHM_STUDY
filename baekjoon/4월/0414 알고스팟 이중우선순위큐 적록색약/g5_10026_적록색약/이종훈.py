from collections import deque
import sys
sys.stdin=open('input.txt')
def search(x,y): #큐도 써보고 써보고 visited도 써봄
    q.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1] #응애
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<N and 0<=ny<N and map[nx][ny] == map[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1  # 방문체크 후 큐에 넣음
                q.append((nx,ny))

def search2(x,y):
    q.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited2[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<N and 0<=ny<N and map[nx][ny] == map[x][y] and visited2[nx][ny] == 0:
                visited2[nx][ny] = 1  # 방문체크 후 큐에 넣음
                q.append((nx,ny))


#-----------------------------------------함수끝--------------------------------------------------------------
N = int(input())
map = [list(input()) for _ in range(N)]
q = deque()


visited = [[0] * N for _ in range(N)] #정상 visited
cnt = 0 #정상 cnt
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:  # 방문 체크
            search(i,j)
            cnt += 1


for i in range(N):
    for j in range(N):
        if map[i][j] == 'G': #Green을 다 RED로 밀어준다
            map[i][j] = 'R'

visited2 = [[0] * N for _ in range(N)] #적록색약의 visited
cnt2 = 0 #적록색약의 cnt
for i in range(N):
    for j in range(N):
        if visited2[i][j] == 0:
            search2(i,j)
            cnt2 += 1

print(cnt, cnt2)