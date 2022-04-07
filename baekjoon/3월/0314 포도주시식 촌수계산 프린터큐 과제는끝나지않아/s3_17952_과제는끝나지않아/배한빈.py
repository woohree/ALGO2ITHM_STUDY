# 과제는 가장 최근에 나온 순서대로 한다. 또한 과제를 받으면 바로 시작한다.
# 과제를 하던 도중 새로운 과제가 나온다면, 하던 과제를 중단하고 새로운 과제를 진행한다.
# 새로운 과제가 끝났다면, 이전에 하던 과제를 이전에 하던 부분부터 이어서 한다.
# (성애는 기억력이 좋기 때문에 아무리 긴 시간이 지나도 본인이 하던 부분을 기억할 수 있다.)

# 10분
# 채점이 1,2분 걸리는거 같다.

import sys
sys.stdin = open('B.txt')

N = int(sys.stdin.readline().rstrip())
task = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

stack = []
total_score = 0
for i in range(N):
    # 과제의 i번 째가 0이 아닐 경우
    # 과제를 받자마자 일단 1분 소요해서 푼다.
    if task[i][0] != 0:
        stack.append(task[i])
        stack[-1][2] -= 1

    # stack이 비어 있지 않으면서, 과제의 i번 째가 0일 경우
    # 과제를 안 받은 경우이므로 stack의 마지막에 있는 과제를 1분 소요해서 푼다.
    elif stack and task[i][0] == 0:
        stack[-1][2] -= 1

    # stack이 비어 있지 않으면서, stack의 마지막 값이 다 풀었을 경우
    # 마지막에 받은 과제를 다 푼 경우이므로 점수를 더하고 stack에서 빼준다.
    if stack and stack[-1][2] == 0:
        total_score += stack[-1][1]
        stack.pop()

print(total_score)
