

# 효율성 통과x
# def solution(board, skill):
#     answer = len(board) * len(board[0])
#     for s in skill:
#         t, r1, c1, r2, c2, deg = s
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 pre_value = board[i][j]
#                 if t == 1:
#                     board[i][j] -= deg
#                     if pre_value > 0 and board[i][j] < 1:
#                         answer -= 1
#                 else:
#                     board[i][j] += deg
#                     if pre_value < 1 and board[i][j] > 0:
#                         answer += 1
#
#     return answer


# IMOS 알고리즘 적용 => 효율성 통과
def solution(board, skill):
    answer = 0
    temp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]  # 누적합 저장할 리스트

    for s in skill:
        t, r1, c1, r2, c2, deg = s
        if t == 1:                              # 시점과 종점에 누적합 표시
            temp[r1][c1] += -deg
            temp[r2+1][c1] += deg
            temp[r1][c2+1] += deg
            temp[r2+1][c2+1] += -deg
        else:
            temp[r1][c1] += deg
            temp[r2+1][c1] += -deg
            temp[r1][c2+1] += -deg
            temp[r2+1][c2+1] += deg

    for i in range(len(temp)-1):                # 표시한 인덱스의 값을 통해 누적합 계산(가로)
        for j in range(len(temp[0])-1):
            temp[i][j+1] += temp[i][j]
    for j in range(len(temp[0])-1):             # 세로
        for i in range(len(temp)-1):
            temp[i+1][j] += temp[i][j]

    for i in range(len(board)):                 # 구한 누적합을 board에 적용
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:                 # 파괴되지 않은 건물 체크
                answer += 1
    print(temp)

    return answer


board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))