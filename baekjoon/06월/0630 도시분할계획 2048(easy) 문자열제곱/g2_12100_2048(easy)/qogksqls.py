import sys
sys.stdin = open('B.txt')

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def solution1(a):
    temp = [[0] * N for _ in range(N)]
    row = [0] * N
    for i in range(N):
        for j in range(N):
            if a[i][j]:
                if row[j]:
                    if row[j] == a[i][j]:
                        row[j] += a[i][j]
                        k = 0
                        while k < N:
                            if not temp[k][j]:
                                temp[k][j] = row[j]
                                break
                            k += 1
                        row[j] = 0
                    else:
                        k = 0
                        while k < N:
                            if not temp[k][j]:
                                temp[k][j] = row[j]
                                break
                            k += 1
                        row[j] = 0
                        row[j] += a[i][j]
                else:
                    row[j] += a[i][j]
    for j in range(N):
        k = 0
        while k < N:
            if not temp[k][j]:
                temp[k][j] = row[j]
                break
            k += 1
    return temp


def solution2(a):
    temp = [[0] * N for _ in range(N)]
    row = [0] * N
    for i in range(N-1, -1, -1):
        for j in range(N):
            if a[i][j]:
                if row[j]:
                    if row[j] == a[i][j]:
                        row[j] += a[i][j]
                        k = N-1
                        while k < N:
                            if not temp[k][j]:
                                temp[k][j] = row[j]
                                break
                            k -= 1
                        row[j] = 0
                    else:
                        k = N-1
                        while k < N:
                            if not temp[k][j]:
                                temp[k][j] = row[j]
                                break
                            k -= 1
                        row[j] = 0
                        row[j] += a[i][j]
                else:
                    row[j] += a[i][j]
    for j in range(N):
        k = N-1
        while k < N:
            if not temp[k][j]:
                temp[k][j] = row[j]
                break
            k -= 1
    return temp


def solution3(a):
    temp = [[0] * N for _ in range(N)]
    col = [0] * N
    for i in range(N):
        for j in range(N):
            if a[j][i]:
                if col[j]:
                    if col[j] == a[j][i]:
                        col[j] += a[j][i]
                        k = 0
                        while k < N:
                            if not temp[j][k]:
                                temp[j][k] = col[j]
                                break
                            k += 1
                        col[j] = 0
                    else:
                        k = 0
                        while k < N:
                            if not temp[j][k]:
                                temp[j][k] = col[j]
                                break
                            k += 1
                        col[j] = 0
                        col[j] += a[j][i]
                else:
                    col[j] += a[j][i]
    for j in range(N):
        k = 0
        while k < N:
            if not temp[j][k]:
                temp[j][k] = col[j]
                break
            k += 1
    return temp


def solution4(a):
    temp = [[0] * N for _ in range(N)]
    col = [0] * N
    for i in range(N-1, -1, -1):
        for j in range(N):
            if a[j][i]:
                if col[j]:
                    if col[j] == a[j][i]:
                        col[j] += a[j][i]
                        k = N-1
                        while k < N:
                            if not temp[j][k]:
                                temp[j][k] = col[j]
                                break
                            k -= 1
                        col[j] = 0
                    else:
                        k = N-1
                        while k < N:
                            if not temp[j][k]:
                                temp[j][k] = col[j]
                                break
                            k -= 1
                        col[j] = 0
                        col[j] += a[j][i]
                else:
                    col[j] += a[j][i]
    for j in range(N):
        k = N-1
        while k < N:
            if not temp[j][k]:
                temp[j][k] = col[j]
                break
            k -= 1
    return temp


def dfs(arr, c):
    global my_max
    if c <= 5:
        r_max = 0
        for r in arr:
            r_max = max(r_max, max(r))
        my_max = max(my_max, r_max)
    else:
        return
    for s in solutions:
        t = s(arr)
        if arr != t:
            dfs(t, c + 1)


solutions = [solution1, solution2, solution3, solution4]
my_max = 0
dfs(matrix, 0)
print(my_max)
