import sys
sys.stdin = open('G.txt')

def get_count(N):
    # 대포알이 한개일때 만들 수 있는 것
    nums = [1, 1, 1]
    # 사면체를 만들때 필요한 대포알 개수
    # [1, 4, 10, 20, ...]
    figure_cnt = [1]
    # 종료 조건 설정 위해 선언
    num = 1
    i = 1
    while num < N:
        i += 1
        triangle = nums[1] + i
        num = nums[2] + triangle
        nums = [i, triangle, num]
        figure_cnt.append(num)
    
    dp = [999] * (N + 1)

    for i in range(1, N+1):
        for cnt in figure_cnt:
            # 대포알의 개수와 사면체를 만든 대포알의 개수가 같다면,
            if cnt == i:
                dp[i] = 1
                break
            # 대포알의 개수보다 사면체의 개수가 크다면 만들 수 없음
            if i < cnt:
                break
            # +1 하는 이유는 층이 1개인 사면체 추가
            # 대포알의 개수와 사면체를 만드는데 필요한 대포알의 개수가 완전히 같지 않기 때문
            dp[i] = min(dp[i], 1 + dp[i-cnt])
    
    return dp[-1]


N = int(sys.stdin.readline().rstrip())
answer = get_count(N)
print(answer)