import sys
sys.stdin = open('B.txt')

'''
움직이지 않아도 되는 아이들 -> 가장 긴 오름차순 수열
'''

N = int(sys.stdin.readline().rstrip())
children = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

dp = [0] * (N + 1)

for child in children:
    dp[child] = max(dp[:child]) + 1

print(N - max(dp))
