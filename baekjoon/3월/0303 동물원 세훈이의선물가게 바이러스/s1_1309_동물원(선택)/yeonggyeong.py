import sys
sys.stdin = open('G.txt')

def get_lion(n):

    # n = 1일때 첫번째 줄 공백, 첫번째 줄 왼쪽에 존재, 첫번째 줄 오른쪽 존재 초기화
    dp = [1, 1, 1]
    # n일때 첫번째 줄 공백의 경우 n-1의 경우의 수
    # n일때 첫번째 줄 왼쪽에 사자가 존재할 경우 n-1의 첫번째 줄 공백 + n-1 첫번째 줄 왼쪽에 사자 존재
    # n일때 첫번째 줄 오른쪽에 사자가 존재할 경우는 왼쪽에 사자가 존재할 경우와 동일
    for _ in range(1, n):
        lst = []
        lst.append(dp[0] + dp[1] + dp[2])
        left_right = dp[0] + dp[1]
        lst.append(left_right)
        lst.append(left_right)
        # dp를 초기화하지않고 추가할 경우 메모리 초과 발생
        dp = lst

    return dp[0] + dp[1] + dp[2]

n = int(input())
answer = get_lion(n)
print(answer % 9901)