import sys
sys.stdin = open('G.txt')

def warshall():
    for k in range(1, N+1):
        matrix[k][k] = 0
        for s in range(1, N+1):
            for e in range(1, N+1):
                matrix[s][e] = min(matrix[s][k] + matrix[k][e], matrix[s][e])


N = int(sys.stdin.readline())

matrix = [[float('inf')] * (N+1) for _ in range(N+1)]

while True:
    f1, f2 = map(int, sys.stdin.readline().split())
    # -1나오면 반복 종료
    if f1 == -1:
        break

    matrix[f1][f2] = 1
    matrix[f2][f1] = 1

warshall()

min_v = 999
for row in range(1, N+1):
    # 각 회장후보들의 가장 먼 관계 찾기
    relations = max(matrix[row][1:])
    # 먼 관계가 현재 회장 후보의 먼 관계보다 작다면 
    if min_v > relations:
        min_v = relations
        result = [row]
    elif min_v == relations:
        result.append(row)

print(min_v, len(result))
print(' '.join(list(map(str, result))))