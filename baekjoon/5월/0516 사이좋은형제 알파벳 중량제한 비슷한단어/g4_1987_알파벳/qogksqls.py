import sys
sys.stdin = open('B.txt')

'''
처음에는 dfs로 풀었다가 시간초과...
근데 사용한 알파벳을 체크하는 과정에서 list나 dict보다 set이 성능이 제일 좋았다.

두번째는 bfs로 풀었는데 사실 첨에 생각 잘 안나서 다른 코드 참고해서 품
기존에 alphabet에 들어있던 요소들이 다 쓰이면 count를 해주던 원래 bfs를 풀던 방식과는 좀 다르게 
이동 가능한 장소를 본 동시에 그때그때 최대길이를 갱신
'''

R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]

# bfs
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
my_max = 1
alphabets = [(0, 0, board[0][0])]
while alphabets:
    r, c, current = alphabets.pop()  # 'IEFCJ'
    if my_max == 26:
        break
    for move in moves:
        nr = r + move[0]
        nc = c + move[1]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] not in current:
                alphabets.append((nr, nc, current + board[nr][nc]))
                my_max = max(my_max, len(current) + 1)
print(my_max)

'''
def dfs(m, r, c):
    global my_max

    my_max = max(my_max, m)

    for move in moves:
        r += move[0]
        c += move[1]
        if 0 <= r < R and 0 <= c < C:
            if board[r][c] not in alphabets:
                alphabets.add(board[r][c])
                dfs(m+1, r, c)
                alphabets.pop()
        r -= move[0]
        c -= move[1]


moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
alphabets = set(board[0][0])
my_max = 1
dfs(my_max, 0, 0)
print(my_max)
'''