import sys
sys.stdin = open('L.txt')


def get_longest_list(diamonds):
    dp = [0] * N
    for i in range(N):                          # 다이아 리스트를 돌면서,
        longest_length = temp = 1               # 최댓값(longest_length), 비교할 값(temp)
        for j in range(i):                      # 현재 인덱스보다 앞의 인덱스를 돌면서,
            if diamonds[i][0] > diamonds[j][0] and diamonds[i][1] < diamonds[j][1]:  # 조건에 맞다면,
                temp = dp[j] + 1                # 비교할 값을 해당 인덱스의 dp+1 로 갱신하고, 최댓값과 비교
                if temp > longest_length:
                    longest_length = temp
        dp[i] = longest_length                  # 최댓값으로 dp값 갱신

    return max(dp)                              # dp값 중, 가장 큰 값을 반환


T = int(input())
for tc in range(T):
    N = int(input())
    diamonds = [list(map(float, input().split())) for _ in range(N)]
    ans = get_longest_list(diamonds)
    print(ans)