import sys, math
sys.stdin = open('L.txt')


def dfs(n):
    global cnt, weight, j                   # cnt: 가능한 경우의 수, weight: 현재 중량, j: 키트 순서(첫 순서가 N)
    j -= 1
    weight += A[n] - K
    visited[n] = 1

    if weight < 500:                        # 중량이 500보다 작아지면,
        cnt -= math.factorial(j)            # 가능한 경우의 수에서 j! 만큼 빼줌

    elif j > 0:                             # 마지막 순서까지 중량이 500보다 큰 지 검사
        for i in range(N):                  # 키트 조합 만들기
            if not visited[i]:
                dfs(i)

    j += 1
    weight -= A[n] - K
    visited[n] = 0


N, K = map(int, input().split())
A = list(map(int, input().split()))
if sum(A) < N*K:                            # 만약 키트 중량의 합이 K*N보다 작으면,
    print(0)                                # 가능한 경우는 없음
else:
    j = N
    cnt = math.factorial(N)                 # 전체 경우의 수
    visited = [0] * N
    for i in range(N):
        weight = 500
        dfs(i)
    print(cnt)
