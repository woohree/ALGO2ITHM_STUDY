import sys
sys.stdin = open('L.txt')


def dfs(s, e):
    global cnt, n
    if e[0] - s[0] == 1:
        for i in range(s[0], e[0]+1):
            for j in range(s[1], e[1]+1):
                # mat[i][j] = cnt
                if i == r and j == c:
                    return
                cnt += 1
        return

    """
    1. r, c가 있는 사분면으로 파고든다.
    2. 파고들 때마다, 해당 사분면의 좌상단 셀의 값을 계산한다.
    3. 2x2 사이즈가 되면, (r, c) 좌표의 값을 계산한다.
    """

    base = (2**n)**2 // 4                                           # 해당 사분면 좌상단 셀의 값을 계산하기 위한 베이스
    n -= 1                                                          # 사분면 하나 파고들 때마다, n -= 1
    length = (e[0]+1 - s[0]) // 2                                   # 한 변 길이의 절반

    if s[0] <= r < e[0]-length+1 and s[1] <= c < e[1]-length+1:     # 좌상
        cnt += base * 0                                             # 해당 사분면 좌상단 셀의 값
        dfs(s, (e[0]-length, e[1]-length))                          # 시작좌표와 끝좌표를 인자로 넘김
    elif s[0] <= r < e[0]-length+1 and s[1]+length <= c < e[1]+1:   # 우상
        cnt += base * 1
        dfs((s[0], s[1]+length), (e[0]-length, e[1]))
    elif s[0]+length <= r < e[0]+1 and s[1] <= c < e[1]-length+1:   # 좌하
        cnt += base * 2
        dfs((s[0]+length, s[1]), (e[0], e[1]-length))
    else:                                                           # 우하
        cnt += base * 3
        dfs((s[0]+length, s[1]+length), e)


N, r, c = map(int, input().split())
# mat = [[0]*(2**N) for _ in range(2**N)]
cnt = 0
n = N
start, end = (0, 0), (2**N-1, 2**N-1)
dfs(start, end)
print(cnt)