def solution2(r, c, l, arr, answer):
    n, flag = arr[r][c], 0  # 2사분면
    for i in range(r, r + l // 2):
        for j in range(c, c + l // 2):
            if arr[i][j] != n:
                flag = 1
                solution2(r, c, l // 2, arr, answer)
                break
        if flag:
            break
    if not flag:
        answer[n] += 1
    n, flag = arr[r + l // 2][c], 0  # 3사분면
    for i in range(r + l // 2, r + l):
        for j in range(c, c + l // 2):
            if arr[i][j] != n:
                flag = 1
                solution2(r + l // 2, c, l // 2, arr, answer)
                break
        if flag:
            break
    if not flag:
        answer[n] += 1
    n, flag = arr[r][c + l // 2], 0  # 1사분면
    for i in range(r, r + l // 2):
        for j in range(c + l // 2, c + l):
            if arr[i][j] != n:
                flag = 1
                solution2(r, c + l // 2, l // 2, arr, answer)
                break
        if flag:
            break
    if not flag:
        answer[n] += 1
    n, flag = arr[r + l // 2][c + l // 2], 0  # 4사분면
    for i in range(r + l // 2, r + l):
        for j in range(c + l // 2, c + l):
            if arr[i][j] != n:
                flag = 1
                solution2(r + l // 2, c + l // 2, l // 2, arr, answer)
                break
        if flag:
            break
    if not flag:
        answer[n] += 1
    return


def solution(arr):
    answer = [0, 0]
    l = len(arr[0])
    n, flag = arr[0][0], 0  # 전체
    for i in range(l):
        for j in range(l):
            if arr[i][j] != n:
                flag = 1
                break
        if flag:
            break
    if not flag:
        answer[n] += 1
    else:
        solution2(0, 0, l, arr, answer)
    print(answer)
    return answer


x = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
solution(x)
