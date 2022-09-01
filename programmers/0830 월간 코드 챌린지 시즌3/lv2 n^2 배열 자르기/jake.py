def solution(n, left, right):
    # 표에 의하면 matrix[i][j]의 i, j 중 큰 값+1이 matrix[i][j] 값이다
    # 즉 순서대로 배치한 숫자를 n으로 나눈 몫과 나머지가 각각 i, j 가 되니까 거기에 +1 해주면 됨
    answer = []
    idx = left
    while idx <= right:
        a = idx//n
        b = idx%n
        answer.append(max(a, b)+1)
        idx += 1
    return answer