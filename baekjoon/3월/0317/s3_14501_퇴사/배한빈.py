import sys
sys.stdin = open('B.txt')


def get_answer():
    global answer
    for i in range(N):
        if counseling[i][0] + i <= N:
            temp = 0
            for j in range(i):
                if dp[j][0] <= i and dp[j][1] > temp:
                    temp = dp[j][1]
            dp[i][0] = i + counseling[i][0]
            dp[i][1] = temp + counseling[i][1]
    for k in range(N):
        if answer < dp[k][1]:
            answer = dp[k][1]


N = int(input())
counseling = [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0] for _ in range(N)]

answer = 0
get_answer()

print(answer)
