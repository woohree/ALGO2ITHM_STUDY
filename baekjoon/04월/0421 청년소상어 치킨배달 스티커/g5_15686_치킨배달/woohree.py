import sys, itertools
sys.stdin = open('L.txt')


def get_dakzip_dist_of_city(dakzips):
    result = 0
    for r_home, c_home in homes:                # 각 집 돌면서,
        dist = 2*N+1
        for r_dakzip, c_dakzip in dakzips:
            d = abs(r_home-r_dakzip) + abs(c_home-c_dakzip)
            if d < dist:                        # 집까지의 거리가 더 작으면 갱신!
                dist = d
        result += dist                          # 합에 추가!

    return result


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

dakzips, homes = [], []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 2:                      # 닭집 위치
            dakzips.append((i, j))
        elif mat[i][j] == 1:                    # 집 위치
            homes.append((i, j))

open_dakzips = list(itertools.combinations(dakzips, M))     # 오픈할 수 있는 닭집 경우의 수
min_dakzip_dist_of_city = 1400
for dakzips in open_dakzips:                     # 오픈한 닭집 중,
    dakzip_dist_of_city = get_dakzip_dist_of_city(dakzips)  # 각 집까지 치킨거리의 합(=도시의 치킨거리) 구하기
    if dakzip_dist_of_city < min_dakzip_dist_of_city:       # 작으면 갱신!
        min_dakzip_dist_of_city = dakzip_dist_of_city

print(min_dakzip_dist_of_city)