import sys
sys.stdin = open('M.txt')


def get_minimum():
    dp = [float('inf')] * (N + 1)

    for i in range(1, N + 1):
        for t in totals:
            if t == i:
                dp[i] = 1
                break
            if t > i:
                break

            if dp[i] > dp[i - t] + 1:
                dp[i] = dp[i - t] + 1

    print(dp[N])


T = int(input())

for tc in range(T):
    # 대포알의 개수
    N = int(input())
    count = 0

    totals = []
    i = j = total = 1

    # 합을 미리 계산
    while total <= N:
        totals.append(total)
        i += 1
        j += i
        total += j

    get_minimum()
