import sys
sys.stdin = open('L.txt')


"""
결국 종료시각 기준으로 빠른 순으로 회의를 순서대로 하는 것이 최선의 방법이다. 단, 겹치지 않는 선에서.
1. 종료시각 기준으로 오름차순 정렬한다.
2. 순서대로 갯수를 세되, 앞 회의 종료시각보다 지금 할 회의의 시작시각이 빠르면 안된다.

사실 오늘 풀었던 문제 까먹기 전에 날먹^^ 
"""


def get_maximum_conference(schedule):
    schedule.sort(key=lambda x: (x[1], x[0]))       # 종료시각, 시작시각 순으로 오름차순 정렬
    temp = schedule[0][1]                           # 전 회의의 종료시각 기록
    cnt = 1                                         # 총 회의 수
    for i in range(1, N):
        if schedule[i][0] >= temp:                  # 앞 회의 종료시각과 지금 할 회의 시작시각을 비교
            temp = schedule[i][1]                   # 종료시각 갱신
            cnt += 1
    return cnt


N = int(sys.stdin.readline().rstrip())
schedule = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
ans = get_maximum_conference(schedule)
print(ans)