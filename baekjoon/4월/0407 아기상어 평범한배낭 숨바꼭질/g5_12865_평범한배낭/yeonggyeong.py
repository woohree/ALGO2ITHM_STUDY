import sys
sys.stdin = open('G.txt')

N, K = map(int, input().split())

dp = [0 for _ in range(K+1)]

for _ in range(N):
    w, v = map(int, input().split())

    # 최대 무게부터 현재 짐의 무게까지 역순으로 반복
    for j in range(K, w-1, -1):
        # 가방의 한계가 j일때 dp[한계]와 dp[한계 - 현재 짐의 무게] + 현재 짐의 가치 중 큰 값
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[-1])
