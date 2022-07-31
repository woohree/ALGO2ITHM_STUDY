import sys, copy
from collections import deque
sys.stdin = open('B.txt')


'''
1. 인접한 두 나라의 차가 L, R 사이여야 함
2. bfs 사용해서 풀이
3. bfs 돌면서 조건에 충족하는 나라들 좌표는 리스트에 저장하고 나중에 for 문 돌려서 값 바꿔줌
'''


def bfs(row, col):
    countries = []
    people = 0
    q = deque()
    q.append((row, col))
    countries.append((row, col))
    people += matrix[row][col]
    while q:
        r, c = q.popleft()
        for move in moves:
            next_r = r + move[0]
            next_c = c + move[1]
            if 0 <= next_r < N and 0 <= next_c < N:
                if L <= abs(matrix[r][c] - matrix[next_r][next_c]) <= R and visited[next_r][next_c] == 0:
                    q.append((next_r, next_c))
                    countries.append((next_r, next_c))
                    people += matrix[next_r][next_c]
                    visited[next_r][next_c] = 1
    len_countries = len(countries)
    for country in countries:
        matrix[country[0]][country[1]] = people // len_countries
    return


N, L, R = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

ans = 0
while 1:
    check = copy.deepcopy(matrix)
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)
    if check == matrix:
        break
    ans += 1
print(ans)
