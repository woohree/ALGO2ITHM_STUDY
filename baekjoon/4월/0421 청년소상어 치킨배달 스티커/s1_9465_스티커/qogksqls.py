import sys
sys.stdin = open('B.txt')

# 그림으로 설명

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    stickers = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2)]

    dp1 = [stickers[0][0]]
    dp2 = [stickers[1][0]]
    for i in range(1, n):
        if i == 1:
            dp1.append(dp1[-1] + stickers[i%2][i])
            dp2.append(dp2[-1] + stickers[(i+1)%2][i])
        else:
            if dp1[-1] >= dp2[-1]:
                dp1.append(dp1[-1] + stickers[i%2][i])
                dp2.append(max(dp2[-1], dp1[i-2]) + stickers[(i+1)%2][i])
            else:
                dp2.append(dp2[-1] + stickers[(i+1)%2][i])
                dp1.append(max(dp1[-1], dp2[i-2]) + stickers[i%2][i])

    if dp1[-1] >= dp2[-1]:
        print(dp1[-1])
    else:
        print(dp2[-1])
