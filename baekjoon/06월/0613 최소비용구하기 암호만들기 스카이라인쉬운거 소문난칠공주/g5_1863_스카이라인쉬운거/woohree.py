import sys
sys.stdin = open('L.txt')


n = int(input())
visited = [0]                   # 처음 비교군 필요
cnt = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    if y > visited[-1]:         # 마지막 건물의 높이보다 현재 높이가 크면,
        cnt += 1                # 건물수 +1
        visited.append(y)       # 방문 건물리스트 갱신

    else:                       # 그 외,
        while y < visited[-1]:  # 현재 높이보다 큰 건물들 전부 pop
            visited.pop()

        if y > visited[-1]:     # 지운 뒤, 마지막 건물이 현재 높이보다 작은 경우만,
            cnt += 1            # 건물수 +1
            visited.append(y)   # 갱신
print(cnt)
