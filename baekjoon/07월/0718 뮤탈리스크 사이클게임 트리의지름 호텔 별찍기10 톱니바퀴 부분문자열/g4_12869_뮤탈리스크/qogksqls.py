import sys
from collections import deque
sys.stdin = open('B.txt')

'''
40분
1. dp로 어떻게 푸나 고민하는 시간이 길었는데 결국 dp로 안풀었다.
2. bfs 방식으로 풀었고, scv 중 가장 체력이 높은 scv에 9를 무조건적으로 빼야하는 조건만 넣었다.
3. 경우의 수가 6가지밖에 없고, 최대 체력이 60밖에 안되서 dp 안 쓰고 해결 가능했다.
'''

N = int(sys.stdin.readline().rstrip())
SCV = list(map(int, sys.stdin.readline().rstrip().split()))
while len(SCV) < 3:
    SCV.append(0)

cases = [
    (9, 3, 1),
    (9, 1, 3),
    (3, 9, 1),
    (3, 1, 9),
    (1, 9, 3),
    (1, 3, 9),
]
ans = 0
q = deque()
q.append(SCV[:])
while q:
    for _ in range(len(q)):
        scv = q.popleft()
        for i in range(6):
            temp = scv[:]
            if cases[i].index(9) != temp.index(max(temp)):  # 2번
                continue
            flag = 1
            temp[0] -= cases[i][0]
            temp[1] -= cases[i][1]
            temp[2] -= cases[i][2]
            for j in temp:  # scv 다 죽였나 검사
                if j > 0:
                    flag = 0
                    break
            if flag:
                print(ans + 1)
                exit()
            q.append(temp)
    ans += 1
