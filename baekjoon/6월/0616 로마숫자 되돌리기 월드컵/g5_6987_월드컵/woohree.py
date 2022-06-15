import sys
sys.stdin = open('L.txt')


def dfs(now, new):                          # now vs new
    global check
    if new == 6:                            # 상대팀이 6번이면(존재x)
        now += 1                            # 현재 팀을 하나 오른쪽으로 바꾸기
        new = now + 1

    if now == 5:                            # 현재팀이 5번이면, 끗!(상대팀x)
        return 1

    for now_i in range(3):
        if teams[now][now_i]:               # 현재팀 인덱스(승무패)가 0보다 크면,
            if now_i == 0:                  # 승이면, 상대는 패
                new_i = 2
            elif now_i == 1:                # 무면, 상대는 무
                new_i = 1
            else:                           # 패면, 상대는 승
                new_i = 0
            if teams[new][new_i]:           # 상대팀 인덱스(승무패)가 0보다 크면,
                teams[now][now_i] -= 1      # 현재팀 승무패 -1
                teams[new][new_i] -= 1      # 상대팀 승무패 -1
                if dfs(now, new+1):         # 다음 상대팀 찾아가기
                    return 1
                teams[now][now_i] += 1      # 승무패 원상복구
                teams[new][new_i] += 1
    return 0                                # 다했는데 숫자 남았으면 불가능!


ans = []
for _ in range(4):
    results = list(map(int, input().split()))
    if 6 in results:                        # 전체 팀이 6갠데, 한 팀이 6승, 6무, 6패는 불가능
        ans.append(0)
        continue
    teams = [results[i*3:i*3+3] for i in range(6)]
    # print(teams)
    check = dfs(0, 1)
    ans.append(check)

print(*ans)