import heapq
import sys
sys.stdin = open('M.txt')


def beer_festival():
    hq = []
    preference = 0                  # 선호도의 합 저장
    for beer in beers:
        heapq.heappush(hq, beer)
        preference += beer[0]
        if len(hq) == N:
            if preference >= M:
                print(beer[1])
                break
            else:
                preference -= heapq.heappop(hq)[0]
    else:
        print(-1)


# 축제 기간 N, 선호도의 최소 합 M, 맥주 종류 K
N, M, K = map(int, input().split())
# 맥수 도수, 선호도 오름차순 정렬
beers = sorted([list(map(int, input().split())) for _ in range(K)], key=lambda x: (x[1], x[0]))
beer_festival()
