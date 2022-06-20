import sys
sys.stdin = open('B.txt')

M, N = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(M)]

garo_count, sero_count = 0, 0
for i in range(M-1):
    top, bottom = 0, 0
    for j in range(N):
        if matrix[i][j] == 'X':
            if matrix[i+1][j] == '.':
                if bottom:
                    garo_count += 1
                    bottom -= 1
                else:
                    bottom += 1
            else:
                if bottom:
                    bottom -= 1
            top = 0
        elif matrix[i][j] == '.':
            if matrix[i+1][j] == 'X':
                if top:
                    garo_count += 1
                    top -= 1
                else:
                    top += 1
            else:
                if top:
                    top -= 1
            bottom = 0
for j in range(N-1):
    left, right = 0, 0
    for i in range(M):
        if matrix[i][j] == 'X':
            if matrix[i][j + 1] == '.':
                if right:
                    sero_count += 1
                    right -= 1
                else:
                    right += 1
            else:
                if right:
                    right -= 1
            left = 0
        elif matrix[i][j] == '.':
            if matrix[i][j + 1] == 'X':
                if left:
                    sero_count += 1
                    left -= 1
                else:
                    left += 1
            else:
                if left:
                    left -= 1
            right = 0
print(garo_count + sero_count)
