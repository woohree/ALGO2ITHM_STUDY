import sys
sys.stdin = open('M.txt')

N = int(sys.stdin.readline())
tasks, selected = [], []    # 과제 목록 tasks, 선택 과제 selected
for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())   # 과제 마감일까지 남은 일수 d, 과제 점수 w
    tasks.append((d, w))
tasks.sort(key=lambda x: x[0], reverse=True)

while tasks:
    cd, cw = tasks.pop()
    if len(selected) < cd:          # 과제 마감일까지 남은 일수보다 선택된 과제가 적을 때
        selected.append(cw)
        selected.sort(reverse=True)
    elif selected[-1] < cw:      # 점수가 더 높은 과제가 있을 때
        selected.pop()
        selected.append(cw)
        selected.sort(reverse=True)

print(sum(selected))
