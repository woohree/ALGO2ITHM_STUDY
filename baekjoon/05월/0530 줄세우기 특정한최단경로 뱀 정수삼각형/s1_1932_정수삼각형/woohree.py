import sys
sys.stdin = open('L.txt')


def dp(triangle):
    for i in range(1, n):           # 행
        for j in range(i+1):        # 열
            if j == 0:              # 가장 왼쪽 숫자 => 이전 행의 가장 왼쪽 수만 가능
                triangle[i][j] += triangle[i-1][j]
            elif j == i:            # 가장 오른쪽 숫자 => 이전 행의 가장 오른쪽 수만 가능
                triangle[i][j] += triangle[i-1][j-1]
            else:                   # 그외, 가능한 이전 행까지의 합 중, 더 큰 수를 취함
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return triangle


n = int(input())
triangle = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
ans = max(dp(triangle)[n-1])        # 마지막 행까지의 합 중, 가장 큰 수를 출력
print(ans)