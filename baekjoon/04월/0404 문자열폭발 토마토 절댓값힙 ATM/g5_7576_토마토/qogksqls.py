# bfs 사용
# 골5치고 쉽게 느껴진 문제
# 처음에 visited 만들고 풀었지만 그냥 처음 주어진 matrix 를 사용하면 된다.

import sys, collections
sys.stdin = open('B.txt')


def bfs():
    global answer
    while tomatoes:
        # 우현님이 알려주신 deque 쓸때 for 문 사용법
        for _ in range(len(tomatoes)):
            tomato = tomatoes.popleft()
            for move in moves:
                if 0 <= tomato[0] + move[0] < N and 0 <= tomato[1] + move[1] < M:
                    if boxes[tomato[0] + move[0]][tomato[1] + move[1]] == 0:
                        tomatoes.append((tomato[0] + move[0], tomato[1] + move[1]))
                        boxes[tomato[0] + move[0]][tomato[1] + move[1]] = 1
        answer += 1


M, N = map(int, sys.stdin.readline().rstrip().split())
boxes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

tomatoes = collections.deque()

# deque에 초기에 익은 토마토의 좌표를 미리 입력
for row in range(N):
    for col in range(M):
        if boxes[row][col] == 1:
            tomatoes.append((row, col))

# bfs 함수 내부에서 익은 토마토를 다 체크했는데 마지막에 한 번 더 계산하는 과정이 있으므로 -1부터 시작해야 답 나옴
answer = -1
bfs()

for row in boxes:
    if 0 in row:
        print(-1)
        break
# 주리님이 알려주신 for 문 뒤에 else 쓰기
else:
    print(answer)
