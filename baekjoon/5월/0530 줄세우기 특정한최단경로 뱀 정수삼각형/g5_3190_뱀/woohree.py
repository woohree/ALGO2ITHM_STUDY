import sys
from collections import deque
sys.stdin = open('L.txt')


def snake_game(dirs):
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우하좌상(L-, D+)
    t = d = 0                                   # 시간, 방향
    mat[0][0] = 1
    news = []
    news.append((0, 1))
    head, tail = (0, 0), (0, 0)
    tail_dirs = deque()                         # 꼬리 진행 방향
    tail_dirs.append(d)

    while news:
        t += 1
        head = news.pop()
        r, c = head[0], head[1]

        if mat[r][c] == 0:                      # 사과가 없으면, 꼬리도 같이 이동(길이변화x)
            mat[tail[0]][tail[1]] = 0
            tail_dir = tail_dirs.popleft()
            tail = (tail[0] + moves[tail_dir][0], tail[1] + moves[tail_dir][1])
        mat[r][c] = 1                           # 머리는 무조건 이동

        if dirs and dirs[0][0] == t:            # 뱀의 방향 변화 확인
            dir = dirs.popleft()
            if dir[1] == 'D':                   # 우로 턴
                d += 1
            else:                               # 좌로 턴
                d -= 1
            d %= 4

        new_r, new_c = r + moves[d][0], c + moves[d][1]
        if 0 <= new_r < N and 0 <= new_c < N and mat[new_r][new_c] != 1:
            tail_dirs.append(d)                 # 벽이거나, 몸(1)을 만나면 종료
            news.append((new_r, new_c))

    return t


N = int(input())
mat = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    mat[r-1][c-1] = 2                           # 이거 때문에 30분 오류 못찾음 ㅡㅡ
L = int(input())
snake_dirs = deque()
for _ in range(L):
    n, d = sys.stdin.readline().rstrip().split()
    n = int(n)
    snake_dirs.append((n, d))
ans = snake_game(snake_dirs)
print(ans+1)
