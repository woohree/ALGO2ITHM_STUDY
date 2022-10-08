import sys
sys.stdin = open('M.txt')


def max_meeting():
    selected = []

    for meeting in meetings:
        if not selected or selected[-1][1] <= meeting[0]:   # 첫번째로 종료하는 회의이거나, 이전 회의의 종료시간보다 이번 회의의 시작시간이 같거나 늦을 때
            selected.append(meeting)

    return len(selected)


# 7 7 / 4 7     : 종료시간만을 기준으로 정렬했을 때의 반례
N = int(input())
meetings = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))  # 회의 종료시간, 시작시간을 기준으로 오름차순 정렬하여 저장
print(max_meeting())
