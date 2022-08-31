n, k = map(int, input().split())
lists = list(map(int, input().split()))
visit = [0] * n
cnt = 0
answer = 0


def dfs(weight):
    global cnt, ans
    if weight < 500:
        return
    if cnt == n:
        ans += 1
        return

    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1 #기구를 썼니?
            weight = weight - k + lists[i] #-감량 +증량
            cnt += 1
            dfs(weight)
            cnt -= 1


dfs(500)
print(answer)