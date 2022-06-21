import sys
sys.stdin = open('M.txt')


# 세로 길이 M, 가로 길이 N
M, N = map(int, sys.stdin.readline().split())
matrix = []

for _ in range(M):
    matrix.append(list(map(str, sys.stdin.readline().rstrip())))

answer = 0
# 가로
top = bottom = 0
for i in range(M):
    for j in range(N):
        if matrix[i][j] == '.':
            if 0 <= i - 1 and matrix[i - 1][j] == 'X':      # X
                top += 1                                    # .
                if top == 2:
                    answer += 1
                    top = 0
            else:
                top = 0
            if i + 1 < M and matrix[i + 1][j] == 'X':       # .
                bottom += 1                                 # X
                if bottom == 2:
                    answer += 1
                    bottom = 0
            else:
                bottom = 0
        else:
            top = bottom = 0
    top = bottom = 0

# 세로
left = right = 0
for i in range(N):
    for j in range(M):
        if matrix[j][i] == '.':
            if 0 <= i - 1 and matrix[j][i - 1] == 'X':      # X.
                left += 1
                if left == 2:
                    answer += 1
                    left = 0
            else:
                left = 0
            if i + 1 < N and matrix[j][i + 1] == 'X':       # .X
                right += 1
                if right == 2:
                    answer += 1
                    right = 0
            else:
                right = 0
        else:
            left = right = 0
    left = right = 0

print(answer)
