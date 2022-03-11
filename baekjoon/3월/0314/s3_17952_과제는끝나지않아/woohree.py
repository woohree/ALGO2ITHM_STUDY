import sys
sys.stdin = open('L.txt')


def get_score(homeworks):
    if N == 1:                              # N이 1이면, 과제를 해결할 수 없다.
        return 0
    temp = []                               # 스택
    score = 0

    for i in range(N):
        if homeworks[i][0]:                 # 1인 경우,
            temp.append(homeworks[i])       # 스택에 push!

        if temp:                            # 스택에 과제가 있다면,
            temp[-1][2] -= 1                # 1분 동안 과제 진행
            if not temp[-1][2]:             # 과제를 완료했다면,
                score += temp.pop()[1]      # 점수를 더해주고 스택에서 pop!

    return score


N = int(sys.stdin.readline().rstrip())
homeworks = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
ans = get_score(homeworks)
print(ans)
