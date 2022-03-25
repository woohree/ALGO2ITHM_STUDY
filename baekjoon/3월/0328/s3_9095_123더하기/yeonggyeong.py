import sys
sys.stdin = open('G.txt')


def get_count(N):

    dp = [1, 2, 4]

    if N >= 4:
        for i in range(3, N):
            count = dp[i-1] + dp[i-2] + dp[i-3]
            dp.append(count)
    else:
        return dp[N-1]

    return dp[-1]
    

T = int(input())

for tc in range(T):
    N = int(input())
    answer = get_count(N)
    print(answer)

