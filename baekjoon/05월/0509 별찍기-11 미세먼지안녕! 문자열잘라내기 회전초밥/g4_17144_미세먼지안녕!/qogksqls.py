# 100분
import sys
from collections import deque
sys.stdin = open('B.txt')

R, C, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

'''
1. 처음 이중 for 문 돌려서 먼지 있는 좌표(munzies)와 청소기 좌표(dyson)를 저장
2. bfs 방식으로 먼지 확산시켰다.
3. 공기 청정기 위 부분과 아래 부분 따로 함수 만들어서 먼지 이동시켰다.
4. 공기 청정기에 의해 옮겨진 먼지의 현재 좌표들을 munzies에 다시 저장
'''


def diffuse_munzy_bfs():
    my_dict = {}
    for _ in range(len(munzies)):
        current = munzies.popleft()
        check = 0
        temp = matrix[current[0]][current[1]]
        for move in moves:
            next_row = current[0] + move[0]
            next_col = current[1] + move[1]
            if 0 <= next_row < R and 0 <= next_col < C:
                if matrix[next_row][next_col] >= 0:
                    check += 1
                    if my_dict.get((next_row, next_col)):
                        my_dict[(next_row, next_col)] += temp // 5
                    else:
                        my_dict[(next_row, next_col)] = temp // 5

        if my_dict.get(current):
            my_dict[current] += temp - (temp // 5) * check
        else:
            my_dict[current] = temp - (temp // 5) * check

    for k, v in my_dict.items():
        matrix[k[0]][k[1]] = v


def clean_air_up():
    top = dyson[0]
    temp, i = 0, 0
    while 1:
        top[0] += moves[i][0]
        top[1] += moves[i][1]
        if 0 <= top[0] < R and 0 <= top[1] < C:
            if matrix[top[0]][top[1]] == -1:
                return
            temp, matrix[top[0]][top[1]] = matrix[top[0]][top[1]], temp
        else:
            top[0] -= moves[i][0]
            top[1] -= moves[i][1]
            i += 1


def clean_air_bottom():
    bottom = dyson[1]
    temp, i = 0, 0
    while 1:
        bottom[0] += moves_bottom[i][0]
        bottom[1] += moves_bottom[i][1]
        if 0 <= bottom[0] < R and 0 <= bottom[1] < C:
            if matrix[bottom[0]][bottom[1]] == -1:
                return
            temp, matrix[bottom[0]][bottom[1]] = matrix[bottom[0]][bottom[1]], temp
        else:
            bottom[0] -= moves_bottom[i][0]
            bottom[1] -= moves_bottom[i][1]
            i += 1


moves = [[0, 1], [-1, 0], [0, -1], [1, 0]]
moves_bottom = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 1번
munzies = deque()
dyson = []
for r in range(R):
    for c in range(C):
        if matrix[r][c] > 0:
            munzies.append((r, c))
        elif matrix[r][c] == -1:
            dyson.append([r, c])

for _ in range(T):
    diffuse_munzy_bfs()  # 2번
    clean_air_up()       # 3번
    clean_air_bottom()

    # 4번
    for r in range(R):
        for c in range(C):
            if matrix[r][c] > 0:
                munzies.append((r, c))

# 저번에 행렬 전체 값 더하는 방법 있었던 것 같았는데 기억이 안남
answer = 0
for row in matrix:
    answer += sum(row)
print(answer + 2)
