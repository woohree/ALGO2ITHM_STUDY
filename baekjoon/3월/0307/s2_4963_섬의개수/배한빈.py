# 60분 고민하다 포기 + 20분
# DFS나 BFS로 풀어야 할 것 같다.

import sys
sys.stdin = open('B.txt')

# 최대 재귀 깊이를 1,000,000 정도로 크게 설정
sys.setrecursionlimit(10**6)

# 주변 검사
def search_around(i, j):
    global one_count
    global count
    # 마찬가지로 현재 위치 값을 0으로 만들면서 시작
    jido[i][j] -= 1
    one_count += 1
    if 0 < j <= w and 0 < i <= h:
        if jido[i][j+1] == 1:
            count += 1
            search_around(i, j+1)
        if jido[i+1][j+1] == 1:
            count += 1
            search_around(i+1, j+1)
        if jido[i+1][j] == 1:
            count += 1
            search_around(i+1, j)
        if jido[i+1][j-1] == 1:
            count += 1
            search_around(i+1, j-1)
        if jido[i][j-1] == 1:
            count += 1
            search_around(i, j-1)
        if jido[i-1][j-1] == 1:
            count += 1
            search_around(i-1, j-1)
        if jido[i-1][j] == 1:
            count += 1
            search_around(i-1, j)
        if jido[i-1][j+1] == 1:
            count += 1
            search_around(i-1, j+1)
    return

# 섬의 개수를 찾기
def count_island():
    global one_count
    global count
    # 안쪽 if 문에서 현재 위치의 다음 값을 비교하는 식이 있으므로 범위는 h+1, w+1로 한 칸 씩 늘려준다
    for i in range(h+1):
        for j in range(w+1):
            # 1을 발견하면 1을 지워서 중복해서 찾는 것을 방지
            if jido[i][j] == 1:
                jido[i][j] -= 1
                # 1의 개수 카운트
                one_count += 1
                # 지도를 벗어나지 않는 범위 조건 설정
                if 0 < j <= w and 0 < i <= h:
                    # 주변 탐색
                    if jido[i][j+1] == 1:
                        count += 1
                        search_around(i, j+1)
                    if jido[i+1][j+1] == 1:
                        count += 1
                        search_around(i+1, j+1)
                    if jido[i+1][j] == 1:
                        count += 1
                        search_around(i+1, j)
                    if jido[i+1][j-1] == 1:
                        count += 1
                        search_around(i+1, j-1)
                    if jido[i][j-1] == 1:
                        count += 1
                        search_around(i, j-1)
                    if jido[i-1][j-1] == 1:
                        count += 1
                        search_around(i-1, j-1)
                    if jido[i-1][j] == 1:
                        count += 1
                        search_around(i-1, j)
                    if jido[i-1][j+1] == 1:
                        count += 1
                        search_around(i-1, j+1)
    return


while 1:
    w, h = map(int, input().split())
    # w가 0이면 종료
    if w == 0:
        break

    jido = [[0] * (w + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(h)] + [[0] * (w + 2)]

    # one_count: 지도에서 1의 개수를 찾는다
    # count: 이어져 있는 1의 위치를 찾은 횟수
    one_count = count = 0
    count_island()

    # one_count 에서 count 를 빼야 출력 값이 나온다
    print(one_count - count)
