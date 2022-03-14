# 소요시간 : 3-4시간
# 점수 : 12%까지 갔다가 실패라고 뜸

# 주리님 코드 보고 다시 풀기 : 11시40분 시작 - 12:50분 성공
# 주리님 코드 참고하다보니 많이 비슷해졌는데 무슨 문제가 있었는지는 확실히 알았다.
# 1. 함수를 for tc안에서 돌렸었다. 굳이 그럴 필요가 없다는걸 알았다.
# 2. 좌표는 0부터 시작하므로 x의 길이는 총 M+1, y는 N+1이므로 baechu_location을 (M+1)*(N+1)의 크기를 갖는 배열로 만듬
# 3. 결정적으로 31번줄에 return을 쓰는 순간 for로 돌리는 의미가 사라진다. return을 안쓰면 함수가 작동하고 돌아와서 다음 for구간으로 넘어가 계산해준다.

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)  # 재귀함수 쓸 때 기본 깊이 제한 높히는거

# find_baechu함수 설정
# x 좌표 기준으로 왼쪽 오른쪽 배추 심어져 있는 좌표 찾아서 제거
# y 좌표 기준으로 위 아래 배추 심어져 있는 좌표 찾아서 제거
def find_baechu(x, y):
    # 좌표를 벗어난 경우
    if x < 0 or y < 0 or x > M or y > N:
        return

    if baechu_location[x][y] == 0:
        return
    # 탐색 리스트 설정
    tamseaks = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    baechu_location[x][y] -= 1

    for tamsaek in tamseaks:
        if baechu_location[x + tamsaek[0]][y + tamsaek[1]] == 1:
            find_baechu(x + tamsaek[0], y + tamsaek[1])  # return을 쓰는 순간 for로 돌리는 의미가 사라진다. return을 안쓰면 함수가 작동해도 다시 돌아와서 계산해준다.

# 첫째줄 T 받고
T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())  # 둘째줄 split써서 M,N,K 받고

    baechu_location = [[0] * (N + 1) for _ in range(M+1)]  # 좌표는 0부터 시작하므로 x의 길이는 총 M+1, y는 N+1이므로 baechu_location을 (M+1)*(N+1)의 크기를 갖는 배열로 만듬
    for i in range(K):
        x, y = map(int, input().split())
        baechu_location[x][y] += 1   # 배추의 좌표들 list로 받고

    # 오른쪽으로 M만큼, 위로 N만큼 이동하는 이중 for 구문
    # 오른쪽으로 +1, 위로 +1 하는 for구문
    count = 0
    for j in range(N+1):  # y 좌표
        for i in range(M+1):  # x 좌표
            if baechu_location[i][j] == 1:
                count += 1
                find_baechu(i, j)

    print(count)