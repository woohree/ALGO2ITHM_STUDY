import sys
sys.stdin = open('W.txt')


A, B = map(int, input().split())
N, M = map(int, input().split())
dirs = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
mat = [[0]*A for _ in range(B)]
robots = [0]
for i in range(1, N+1):
    x_t, y_t, d = sys.stdin.readline().rstrip().split()
    r, c = (A-1) - int(y_t), int(x_t) - 1
    mat[r][c] = (i, d)
    robots.append((r, c, d))
for _ in range(M):
    idx, command, cnt = sys.stdin.readline().rstrip().split()
    i, cnt = int(idx), int(cnt)
    r, c, d = robots[i]
    for ct in range(1, cnt+1):
        new_r, new_c = r + ct + dirs[d][0], c + ct + dirs[d][1]
        if 0 <= new_r < B and 0 <= new_c < A:
            if not mat[new_r][new_c]:
                mat[r][c] = 0
                r, c = new_r, new_c
                mat[new_r][new_c] = (i, d)
            else:
                print(f'Robot {i} crashes into robot {mat[new_r][new_c][0]}')
                exit()
        else:
            print(f'Robot {i} crashes into the wall')
            exit()
else:
    print('OK')