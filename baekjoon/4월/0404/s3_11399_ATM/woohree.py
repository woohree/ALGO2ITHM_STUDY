import sys
sys.stdin = open('L.txt')


"""
회의실 배정과 비슷한 문제
여기서 빨리 인출하는 사람이 회의실 배정에서 종료시간이 짧은 사람과 같은 의미
따라서, 정렬 후, 누적 합을 구함
"""


def greedy(P):
    result = 0
    for i in range(N):
        result += sum(P[:i+1])

    return result


def greedy_dp(P):
    dp = [P[0]]
    for i in range(1, N):
        dp.append(dp[i-1]+P[i])

    return sum(dp)


N = int(input())
P = list(map(int, input().split()))
P.sort()
ans = greedy_dp(P)
# ans = greedy(P)
print(ans)