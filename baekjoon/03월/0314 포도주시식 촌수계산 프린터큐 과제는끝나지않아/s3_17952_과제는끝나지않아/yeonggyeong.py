import sys
sys.stdin = open('G.txt')

N = int(input())

assignments = [list(map(int, input().split())) for _ in range(N)]

# 현재 진행 중인 과제
progress = []
score = 0
for assignment in assignments:
    # 새로 추가된 과제가 없다면
    if assignment[0] == 0:
        # 진행 중인 과제의 시간이 남았다면
        if progress and progress[-1][1] != 0:
            # 가장 최근 진행 중인 과제의 시간을 -1
            progress[-1][1] -= 1
            # 가장 최근 진행 중인 과제를 끝마쳤다면
            if progress[-1][1] == 0:
                # 점수 추가 및 진행 중 과제에서 제거
                score += progress[-1][0]
                progress.pop(-1)
    else:
        # 1분짜리 과제라면 점수 바로 추가
        if assignment[2] == 1:
            score += assignment[1]
        else:
            # 1분 이상이라면 시간 마이너스하고 추가 -> 받는 순간 1분 지나서
            assignment[2] -= 1
            progress.append(assignment[1:])

print(score)