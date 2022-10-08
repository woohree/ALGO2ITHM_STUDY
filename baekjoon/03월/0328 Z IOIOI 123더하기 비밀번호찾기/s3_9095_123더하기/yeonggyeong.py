import sys
sys.stdin = open('G.txt')


def get_count(N):
    # 1, 2, 3까지 구할 수 있는 개수
    dp = [1, 2, 4]

    if N >= 4:
        # 3부터 N까지 
        for i in range(3, N):
            count = dp[i-1] + dp[i-2] + dp[i-3]
            dp.append(count)

    return dp[N-1]
    

T = int(input())

for tc in range(T):
    N = int(input())
    answer = get_count(N)
    print(answer)

