def solution(m, n, k):
    lst = []
    for _ in range(k):
        lst.append(list(map(int, input().split())))

    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in lst:
        r = i[1]
        c = i[0]
        matrix[r][c] = 1

    result = 0
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 1:
                if matrix[r+1][c] == 0 and matrix[r][c+1] == 0:
                    result += 1

    return result

T = int(input())
answer = []
for tc in range(T):
    m, n, k = map(int, input().split(' '))
    answer.append(solution(m, n, k))

print(answer)