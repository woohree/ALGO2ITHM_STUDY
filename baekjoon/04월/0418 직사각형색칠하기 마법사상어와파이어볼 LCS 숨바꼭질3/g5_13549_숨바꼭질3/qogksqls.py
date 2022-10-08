import sys
sys.stdin = open('B.txt')


def solution(k, time):
    # 누나 위치가 동생 위치보다 크거나 같을 경우, 두 위치의 차이를 return
    if k <= N:
        return time + N - k

    # 누나 위치가 동생 위치보다 작지만 재귀가 계속 멈추지 않는 경우는 동생이 1일 경우, 1을 return
    elif k == 1:
        return time + 1

    # 위 조건을 피하면서 동생이 홀수일 경우에는, 동생 위치에 +1한 재귀와 -1한 재귀를 각각 비교한다.
    elif k % 2:
        return min(solution(k + 1, time + 1), solution(k - 1, time + 1))
    # 동생 위치가 짝수일 경우엔 2로 나눠 재귀 돌린 값과 time + (동생 위치와 누나 위치의 차이) 중 작은 값을 return
    else:
        return min(solution(k // 2, time), time + k - N)


N, K = map(int, input().split())

print(solution(K, 0))
