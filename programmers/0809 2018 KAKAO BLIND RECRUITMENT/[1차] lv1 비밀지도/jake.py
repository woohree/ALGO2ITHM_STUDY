def solution(n, arr1, arr2):
    arr1binary = []
    arr2binary = []
    for i in arr1:
        tmp = list(bin(i)[2:])
        while len(tmp) != n:
            tmp.insert(0, '0')
        arr1binary.append(tmp)
    for i in arr2:
        tmp = list(bin(i)[2:])
        while len(tmp) != n:
            tmp.insert(0, '0')
        arr2binary.append(tmp)
    answer = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr1binary[i][j] == '1' or arr2binary[i][j] == '1':
                answer[i][j] = '#'
            elif arr1binary[i][j] == '0' and arr1binary[i][j] == '0':
                answer[i][j] = ' '
    answer2 = []
    for i in range(n):
        answer2.append(''.join(answer[i]))
    return answer2