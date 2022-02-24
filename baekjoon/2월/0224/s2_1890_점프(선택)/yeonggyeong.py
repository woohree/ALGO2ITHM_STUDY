import sys
sys.stdin = open('G.txt')

def get_roads(N, matrix):
    # 각 원소까지 올 수 있는 길을 적는 dp 생성
    dp = [[0] * N for _ in range(N)]

    # 0,0 까지 올 수 있는 경우는 1가지
    dp[0][0] = 1
    for row in range(N):
        for col in range(N):
            # 도착점이라면 함수 종료
            if row == N-1  and col == N-1:
                return dp[row][col]
            else:
                # 몇 칸 갈 수 있는지 확인
                number = matrix[row][col]
                # 인덱스 범위를 넘어가지 않는다면
                # 오른쪽, 아래쪽으로 이동하여 현재 위치까지 올 수 있는 경우의 수 추가
                if row+number < N:
                    dp[row+number][col] += dp[row][col]
                if col+number < N:
                    dp[row][col+number] += dp[row][col]

N = int(input()) 
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = get_roads(N, matrix)
print(answer)