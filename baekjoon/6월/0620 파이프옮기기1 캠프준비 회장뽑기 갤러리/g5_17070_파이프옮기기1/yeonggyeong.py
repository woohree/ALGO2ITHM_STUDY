import sys
sys.stdin = open('G.txt')

def dfs(x, y, direction):
    global result

    if x == n-1 and y == n-1:
        result += 1
    if direction == 0: # 가로이동일때
        # 가로이동
        if 0 <= y + 1 < n and matrix[x][y+1] == 0:
            dfs(x, y+1, 0)
        # 대각선 이동
        if 0 <= x+1 < n and 0 <= y+1 < n and matrix[x+1][y] == 0 and matrix[x][y+1] == 0 and matrix[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)
    elif direction == 1: # 세로이동일때
        # 세로이동
        if 0 <= x+1 < n and matrix[x+1][y] == 0:
            dfs(x+1, y, 1)
        # 대각선 이동
        if 0 <= x+1 < n and 0 <= y+1 < n and matrix[x+1][y] == 0 and matrix[x][y+1] == 0 and matrix[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)
    else:
        # 가로이동
        if 0 <= y + 1 < n and matrix[x][y+1] == 0:
            dfs(x, y+1, 0)
                # 세로이동
        if 0 <= x+1 < n and matrix[x+1][y] == 0:
            dfs(x+1, y, 1)
        # 대각선 이동
        if 0 <= x+1 < n and 0 <= y+1 < n and matrix[x+1][y] == 0 and matrix[x][y+1] == 0 and matrix[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)

n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0

dfs(0, 1, 0)
print(result)