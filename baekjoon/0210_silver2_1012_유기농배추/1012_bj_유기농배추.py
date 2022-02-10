# 소요시간 : 3-4시간
# 점수 : 12%까지 갔다가 실패라고 뜸

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)  # 재귀함수 쓸 때 기본 깊이 제한 높히는거

T = int(input())  # 첫째줄 T 받고
for tc in range(1, T+1):
    MNK_list = list(map(int, input().split(' ')))  # 둘째줄 split써서 M,N,K list로 받고

    baechu_location = []
    for i in range(int(MNK_list[2])):
        baechu_location.append(list(map(int, input().split())))  # 배추의 좌표들 list로 받고

    # find_baechu함수 설정
    # x 좌표 기준으로 왼쪽 오른쪽 배추 심어져 있는 좌표 찾아서 제거
    # y 좌표 기준으로 위 아래 배추 심어져 있는 좌표 찾아서 제거
    def find_baechu(x, y):
        if [x + 1, y] in baechu_location:
            baechu_location.remove([x + 1, y])
            return find_baechu(x + 1, y)
        if [x, y + 1] in baechu_location:
            baechu_location.remove([x, y + 1])
            return find_baechu(x, y + 1)
        if [x - 1, y ] in baechu_location:
            baechu_location.remove([x - 1, y])
            return find_baechu(x - 1, y)
        if [x, y - 1] in baechu_location:
            baechu_location.remove([x, y - 1])
            return find_baechu(x, y - 1)

    # 오른쪽으로 M만큼, 위로 N만큼 이동하는 이중 for 구문
    # 오른쪽으로 +1, 위로 +1 하는 for구문
    # (0, 0)에서 시작
    first_xy = [0, 0]
    count = 0
    for first_xy[1] in range(int(MNK_list[1]+1)):  # y 좌표
        for first_xy[0] in range(int(MNK_list[0]+1)):  # x 좌표
            if first_xy in baechu_location:  # (x,y) 가 baechu_location list에 있으면,
                count += 1  # 배추 있는 좌표 찾을 때마다 count +1
                baechu_location.remove(first_xy)  # 그 자리의 배추 좌표 제거
                find_baechu(first_xy[0], first_xy[1])  # find_baechu 함수 사용

    print(count)
