import sys
from collections import deque
sys.stdin = open('B.txt')

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
apples = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(K)]
L = int(sys.stdin.readline().rstrip())
directions = []
for _ in range(L):
    t, di = sys.stdin.readline().rstrip().split()
    if directions:
        directions.append([int(t) - temp_t, di])
        temp_t = int(t)
    else:
        directions.append([int(t), di])
        temp_t = int(t)
# 이동 인풋 마지막에 벽 끝까지 이동할 수 잇는 값을 하나 추가
directions.append([N+1, 'D'])
'''
0: 우
1: 하
2: 좌
3: 상
'''
now = deque()
now.append([1, 1])
used = []
time = 0
d = 0
flag = 1
for direction in directions:
    for i in range(direction[0]):
        if d == 0:
            time += 1
            temp = [now[-1][0], now[-1][1] + 1]
            if temp[1] > N:
                flag = 0
                break
            if temp in now:
                flag = 0
                break
            now.append(temp)
            if temp not in apples or temp in used:
                now.popleft()
            else:
                used.append(temp)

        elif d == 1:
            time += 1
            temp = [now[-1][0] + 1, now[-1][1]]
            if temp[0] > N:
                flag = 0
                break
            if temp in now:
                flag = 0
                break
            now.append(temp)
            if temp not in apples or temp in used:
                now.popleft()
            else:
                used.append(temp)

        elif d == 2:
            time += 1
            temp = [now[-1][0], now[-1][1] - 1]
            if temp[1] < 1:
                flag = 0
                break
            if temp in now:
                flag = 0
                break
            now.append(temp)
            if temp not in apples or temp in used:
                now.popleft()
            else:
                used.append(temp)

        else:
            time += 1
            temp = [now[-1][0] - 1, now[-1][1]]
            if temp[0] < 1:
                flag = 0
                break
            if temp in now:
                flag = 0
                break
            now.append(temp)
            if temp not in apples or temp in used:
                now.popleft()
            else:
                used.append(temp)
    if direction[1] == 'D':
        d = (d + 1) % 4
    else:
        d = (d + 3) % 4
    if flag == 0:
        break
print(time)
