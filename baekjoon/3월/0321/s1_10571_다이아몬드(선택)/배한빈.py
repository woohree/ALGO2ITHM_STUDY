# w 증가, c 감소
import sys
sys.stdin = open('B.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    diamonds = [list(map(float, input().split())) for _ in range(N)]

    dp = [1 for _ in range(N)]

    # solution
    for i in range(N):
        for j in range(i+1, N):
            # 선명도 & 크기 비교
            if diamonds[i][1] > diamonds[j][1] and diamonds[i][0] < diamonds[j][0]:
                # 조건 만족하면 최대값 비교해서 넣기
                dp[j] = max(dp[j], dp[i] + 1)

    print(max(dp))
