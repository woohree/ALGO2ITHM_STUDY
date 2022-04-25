import copy


# 실패실패실실패패
answer = [0] * 11
ansum = 0

def dfs(n, rian, info):
    global answer, ansum
    for i in range(9, -1, -1):
        if not rian[i] and n > info[i]:
            break
    else:
        rian_sum = info_sum = 0
        for i in range(10):
            if rian[i] and rian[i] > info[i]:
                rian_sum += 10 - i
            else:
                if info[i]:
                    info_sum += 10 - i
        if rian_sum > info_sum and rian_sum > ansum:
            answer = copy.deepcopy(rian)
            answer[-1] = n
            ansum = rian_sum
        return

    for i in range(9, -1, -1):
    # for i in range(10):
        if not rian[i] and n > info[i]:
            rian[i] += info[i]+1
            dfs(n-(info[i]+1), rian, info)
            rian[i] -= info[i]+1


def solution(n, info):
    global answer
    rian = [0] * 11
    dfs(n, rian, info)
    if answer == rian:
        return [-1]
    return answer

n = 5
info = [3,2,1,1,0,0,0,0,0,0,0]
print(solution(n, info))