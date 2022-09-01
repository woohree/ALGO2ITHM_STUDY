'''
1. 70분 동안 하다가 구글링. 쿼리를 역순으로 하여 x,y가 나오는 좌표들의 범위를 찾는 아이디어 얻음
'''


def solution(n, m, x, y, queries):
    top, bot, le, ri = x, x, y, y
    queries.reverse()
    answer = 0
    for query in queries:
        if query[0] == 0:
            if ri + query[1] < m:
                ri += query[1]
            else:
                ri = m-1
            if le != 0:
                le += query[1]
        elif query[0] == 1:
            if le - query[1] >= 0:
                le -= query[1]
            else:
                le = 0
            if ri != m-1:
                ri -= query[1]
        elif query[0] == 2:
            if bot + query[1] < n:
                bot += query[1]
            else:
                bot = n-1
            if top != 0:
                top += query[1]
        elif query[0] == 3:
            if top - query[1] >= 0:
                top -= query[1]
            else:
                top = 0
            if bot != n-1:
                bot -= query[1]
        if bot < 0 or ri < 0 or top > n-1 or le > m-1:  # 완전 벗어나는 순간들
            break
    else:
        answer = (bot - top + 1) * (ri - le + 1)
    return answer


solution(1000, 1000, 1, 1, [[0,100001],[2,100001]])

'''
def solution(n, m, x, y, queries):
    matrix = [[1] * m for _ in range(n)]
    for query in queries:
        if query[0] == 0:
            for i in range(n):
                for j in range(m-1):
                    for k in range(query[1]):
                        if j+k+1 > m-1:
                            break
                        matrix[i][j] += matrix[i][j+k+1]
                    matrix[i][j+1] = 0
        elif query[0] == 1:
            for i in range(n):
                for j in range(m-1, 0, -1):
                    for k in range(query[1]):
                        if j-k-1 < 0:
                            break
                        matrix[i][j] += matrix[i][j-k-1]
                    matrix[i][j-1] = 0
        elif query[0] == 2:
            for j in range(m):
                for i in range(n-1):
                    for k in range(query[1]):
                        if i+k+1 > n-1:
                            break
                        matrix[i][j] += matrix[i+k+1][j]
                    matrix[i+1][j] = 0
        elif query[0] == 3:
            for j in range(m):
                for i in range(n-1, 0, -1):
                    for k in range(query[1]):
                        if i-k-1 < 0:
                            break
                        matrix[i][j] += matrix[i-k-1][j]
                    matrix[i-1][j] = 0
    return matrix[x][y]
'''