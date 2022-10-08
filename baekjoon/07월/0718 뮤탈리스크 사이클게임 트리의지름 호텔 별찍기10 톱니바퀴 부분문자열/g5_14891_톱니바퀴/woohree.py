import sys
from collections import deque
sys.stdin = open('W.txt')


def right(idx, direc):
    if idx > 4 or gears[idx-1][2] == gears[idx][6]:     # 오른쪽 최대값 혹은 마주보는 극이 같다면, 탈출
        return

    if gears[idx-1][2] != gears[idx][6]:                # 마주보는 극이 다르다면,
        right(idx+1, -direc)                            # 다음 오른쪽거 보기(방향은 반대로 돌림)
        gears[idx].rotate(direc)                        # 질문검색보다가 로테이트 생각남ㅋㅋ


def left(idx, direc):                                   # right 함수와 이하동문!
    if idx < 1 or gears[idx][2] == gears[idx+1][6]:
        return

    if gears[idx][2] != gears[idx+1][6]:
        left(idx-1, -direc)
        gears[idx].rotate(direc)


gears = [0]
for _ in range(4):
    deq = deque()
    deq.extend(list(map(int, list(input()))))
    gears.append(deq)
# print(gears)
K = int(input())
for _ in range(K):
    # N: 0 / S: 1
    # 1 시계 / -1 반시계
    # 맞닿은 극이 다르면 반대로 회전
    n, d = map(int, input().split())
    right(n+1, -d)                                      # 오른쪽거 검사, 돌리면 반대로 돌려버리기~
    left(n-1, -d)                                       # 왼
    gears[n].rotate(d)                                  # 일단 현재 톱니는 무조건 돌림

ans = 0
for i in range(4):
    ans += 2**i * gears[i+1][0]
print(ans)