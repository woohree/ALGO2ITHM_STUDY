import sys
sys.stdin = open('G.txt')

# EWS -> E : 0.3 / W : 0.2 / S : 0.3
# 0.3 * 0.2 * 0.3 -> 0.018

def crazy(x, y, possibility, count):
    global answer

    now_percent = possibility
    # 이동 횟수와 주어진 이동 횟수가 같으면 answer에 현재 확률 더해주고 함수 종료
    if count == N:
        answer += now_percent
        return 
    
    # 방문한 위치 표시
    matrix[x][y] = 1
    
    # 입력받은 순서대로 동, 서, 남, 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for idx in range(4):
        new_x, new_y = x + dx[idx], y + dy[idx]

        if 0 <= new_x < 2 * N + 1 and 0 <= new_y < 2 * N + 1 and matrix[new_x][new_y] == 0:
            crazy(new_x, new_y, now_percent * possibilities[idx], count+1)
            # 다시 되돌아왔을때 방문하지 않은 것으로 변경
            matrix[new_x][new_y] = 0


inputs = list(map(int, input().split()))

# N * N 행렬
N = inputs[0]

# 정수를 확률로 변경
possibilities = list(map(lambda x: x/100, inputs[1:]))

# matrix 가운데에서 한쪽 방향으로 최대 N번          
matrix = [[0 for _ in range(2*N + 1)] for _ in range(2*N + 1)]

# 시작 위치 정가운데
x, y = N, N

answer = 0
crazy(N, N, 1, 0)
print(answer)