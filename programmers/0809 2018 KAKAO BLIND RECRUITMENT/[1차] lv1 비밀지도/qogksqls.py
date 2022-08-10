def solve_bi(x):                                            # 2진수로 변환
    bi = []
    while x != 0:
        bi.append(x%2)
        x //= 2
    return bi


def solution(n, arr1, arr2):
    result = [[" " for _ in range(n)] for _ in range(n)]    # 결과 행렬
    for i in range(n):
        temp = solve_bi(arr1[i])
        k = n - len(temp)
        for j in range(len(temp)-1, -1, -1):
            if temp[j] == 1:
                result[i][k] = '#'
            k += 1
    for i in range(n):
        temp = solve_bi(arr2[i])
        k = n - len(temp)
        for j in range(len(temp)-1, -1, -1):
            if temp[j] == 1:
                result[i][k] = '#'
            k += 1
    answer = []
    for row in result:
        answer.append(''.join(row))
    return answer