# 또 술 문제구만
# 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

# 100분

import sys
sys.stdin = open('B.txt')

n = int(sys.stdin.readline().rstrip())
wines = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

# dp 초기값 설정
# dp[0]: 0번 숫자가 더해지는 경우, 즉 숫자가 들어가지 않는 경우
# dp[1]: 1번 숫자가 더해지는 경우
# dp[2]: 2번 연속으로 숫자가 더해지는 경우
dp = [0, wines[0], wines[0]]

# 1번째부터 for문 돌림
for i in range(1, len(wines)):
    # 이전 dp의 최댓값을 미리 저장, 나중에 dp[0]에 넣을 것.
    my_max = max(dp)
    # 2번 연속인 경우는 이전에 1번 숫자가 들어간 경우에서 지금 wine값을 넣어 준다.
    dp[2] = dp[1] + wines[i]
    # 1번 연속인 경우는 이전에 0번 숫자가 들어간 경우에서 지금 wine값을 넣어 준다.
    dp[1] = dp[0] + wines[i]
    # 0번 연속인 경우는 이전 값의 최대값을 넣어 준다.
    dp[0] = my_max

# 마지막 출력시 dp의 최대값을 찾아 넣어 준다.
print(max(dp))
