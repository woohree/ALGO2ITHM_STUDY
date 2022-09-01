'''
1. 앞서 여러가지 방법으로 풀었지만 다 시간초과. 최대한 시간을 줄이는게 관건
2. 일단 행렬에 들어가는 숫자는 행과 열 중 큰 숫자가 들어감
3.  i*n+j 는 한 칸의 index 정보
4. left <= i*n+j < right+1 라는 범위 안에서만 찾아서 answer 에 append 시켜주면 됨
'''


def solution(n, left, right):
    answer = []
    flag = 0
    for i in range(left // n, n):
        for j in range(n):
            if left <= i*n+j < right+1:
                if i > j:
                    answer.append(i+1)
                elif i <= j:
                    answer.append(j+1)
            elif i*n+j > right + 1:
                flag = 1  # for 문 탈출
                break
        if flag:
            break
    return answer
