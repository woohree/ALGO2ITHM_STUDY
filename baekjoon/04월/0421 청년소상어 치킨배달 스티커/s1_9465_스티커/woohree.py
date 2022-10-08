import sys
sys.stdin = open('L.txt')


"""
1. dp에는 인덱스 당, 2개의 값이 저장됨
    하나는, 이전 dp 값에 0번 행 값을 더하는 경우,
    나머지는, 이전 dp 값에 1번 행 값을 더하는 경우
    
2. 현재 0번 행 dp값 = (2전 1번 행 dp값 + 현재 0번 행 값) vs (1전 1번 행 dp값 + 현재 0번 행 값) 
   현재 1번 행 dp값 = (2전 0번 행 dp값 + 현재 1번 행 값) vs (1전 0번행 dp값 + 현재 1번 행 값)
   
3. 끝까지 돌려서, 마지막 dp의 0번 행과 1번 행 중, 큰 값을 반환

따라서 tc1의 경우,
50 10 100 20 40
30 50 70 10 60

dp = [(50, 30), (40, 100), (200, 120), (140, 210), (250, 260)]
"""


def sticker(scores, n):
    if n == 1:                  # 길이가 1
        return max(scores[0][0], scores[1][0])
    elif n == 2:                # 길이가 2
        return max(scores[1][0]+scores[0][1], scores[0][0]+scores[1][1])

    dp = [(scores[0][0], scores[1][0]),
          (scores[1][0]+scores[0][1], scores[0][0]+scores[1][1])]

    for i in range(2, n):
        dp.append((max(dp[-1][1]+scores[0][i], dp[-2][1]+scores[0][i]),
                   max(dp[-1][0]+scores[1][i], dp[-2][0]+scores[1][i])))

    return max(dp[-1][0], dp[-1][1])


T = int(input())
for tc in range(T):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(2)]
    ans = sticker(scores, n)
    print(ans)

"""
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80

1
3
3 1 1
1 2 10
"""